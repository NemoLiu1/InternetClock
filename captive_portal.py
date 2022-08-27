import gc
import network
import ubinascii as binascii
import uselect as select
import utime as time
from micropython import const

from captive_dns import DNSServer
from captive_http import HTTPServer
from credentials import Creds

class CaptivePortal:
    AP_IP = "192.168.4.1"
    AP_OFF_DELAY = const(10 * 1000)
    MAX_CONN_ATTEMPTS = 9

    def __init__(self, essid=None):
        self.local_ip = self.AP_IP
        self.sta_if = network.WLAN(network.STA_IF)
        self.ap_if = network.WLAN(network.AP_IF)
        if essid is None:
            essid = b"ESP8266-%s" % binascii.hexlify(self.ap_if.config("mac")[-3:])
        self.essid = essid
        self.creds = Creds()
        self.dns_server = None
        self.http_server = None
        self.poller = select.poll()

        self.conn_time_start = None
        # self.uart = UART(1, 9600)  # UART on
        # self.uart.init()

    # def command(self, cmd, data_h, data_l):
    #     start = 0x7E
    #     version = 0xFF
    #     length = 0x06
    #     feedback = 0x00
    #     checksum = -(version + length + cmd + feedback + data_h + data_l) & 0xFFFF
    #     checksum1 = (checksum >> 8) & 0xFF
    #     checksum2 = checksum & 0xFF
    #     end = 0xEF
    #     data = bytes([start, version, length, cmd, feedback, data_h, data_l, checksum1, checksum2, end])
    #     self.uart.write(data)

    def start_access_point(self):
        # sometimes need to turn off AP before it will come up properly
        self.ap_if.active(False)
        while not self.ap_if.active():
            print("Waiting for access point to turn on")
            self.ap_if.active(True)
            time.sleep(1)
        # IP address, netmask, gateway, DNS
        self.ap_if.ifconfig(
            (self.local_ip, "255.255.255.0", self.local_ip, self.local_ip)
        )
        self.ap_if.config(essid=self.essid, authmode=network.AUTH_OPEN)
        print("AP mode configured:", self.ap_if.ifconfig())

    def connect_to_wifi(self):
        print(
            "Trying to connect to SSID '{:s}' with password {:s}".format(
                self.creds.ssid, self.creds.password
            )
        )
        # self.command(PLAY, 0, CONNECTING)

        # initiate the connection
        self.sta_if.active(True)
        self.sta_if.connect(self.creds.ssid, self.creds.password)

        attempts = 1
        while attempts <= self.MAX_CONN_ATTEMPTS:
            if not self.sta_if.isconnected():
                # self.http_server.wifi_status = b'connecting,' + str(attempts).encode()
                print("Connection attempt {:d}/{:d} ...".format(attempts, self.MAX_CONN_ATTEMPTS))
                time.sleep(2)
                attempts += 1
                if self.http_server:
                    self.http_server.wifi_status = b''
            else:
                if self.http_server:
                    self.http_server.wifi_status = b'connected'
                print("Connected to {:s}".format(self.creds.ssid))
                self.local_ip = self.sta_if.ifconfig()[0]
                return True

        print(
            "Failed to connect to {:s} with {:s}. WLAN status={:d}".format(
                self.creds.ssid, self.creds.password, self.sta_if.status()
            )
        )
        # forget the credentials since they didn't work, and turn off station mode
        self.creds.remove()
        self.sta_if.active(False)
        return False

    def check_valid_wifi(self):
        if not self.sta_if.isconnected():
            if self.creds.load().is_valid():
                # have credentials to connect, but not yet connected
                # return value based on whether the connection was successful
                return self.connect_to_wifi()
            # not connected, and no credentials to connect yet
            return False

        if not self.ap_if.active():
            # access point is already off; do nothing
            return False

        # already connected to WiFi, so turn off Access Point after a delay
        if self.conn_time_start is None:
            self.conn_time_start = time.ticks_ms()
            remaining = self.AP_OFF_DELAY
        else:
            remaining = self.AP_OFF_DELAY - time.ticks_diff(
                time.ticks_ms(), self.conn_time_start
            )
            if remaining <= 0:
                self.ap_if.active(False)
                print("Turned off access point")
        return False

    def captive_portal(self):
        print("Starting captive portal")
        self.start_access_point()
        ssid_list = self.scan_ssid()
        print(ssid_list)

        if self.http_server is None:
            self.http_server = HTTPServer(self.poller, self.local_ip)
            self.http_server.ssid_list = ssid_list
            print("Configured HTTP server")
        if self.dns_server is None:
            self.dns_server = DNSServer(self.poller, self.local_ip)
            print("Configured DNS server")

        try:
            while True:
                gc.collect()
                # check for socket events and handle them
                for response in self.poller.ipoll(1000):
                    sock, event, *others = response
                    is_handled = self.handle_dns(sock, event, others)
                    if not is_handled:
                        self.handle_http(sock, event, others)

                if self.check_valid_wifi():
                    print("Connected to WiFi!")
                    # self.http_server.set_ip(self.local_ip, self.creds.ssid)
                    self.http_server.wifi_status = b'connected'
                    time.sleep(2)
                    # self.dns_server.stop(self.poller)
                    # break

                if not self.ap_if.active():
                    # 连接成功 AP 关闭，就退出程序
                    # self.dns_server.stop(self.poller)
                    break

        except KeyboardInterrupt:
            print("Captive portal stopped")

        self.cleanup()

    def handle_dns(self, sock, event, others):
        if sock is self.dns_server.sock:
            # ignore UDP socket hangups
            if event == select.POLLHUP:
                return True
            self.dns_server.handle(sock, event, others)
            return True
        return False

    def handle_http(self, sock, event, others):
        self.http_server.handle(sock, event, others)

    def cleanup(self):
        print("Cleaning up")
        if self.dns_server:
            self.dns_server.stop(self.poller)
        gc.collect()

    def try_connect_from_file(self):
        if self.creds.load().is_valid():
            if self.connect_to_wifi():
                # self.command(PLAY, 0, CONNECTED)
                # 等待声音播放结束
                time.sleep(2)
                return True

        # WiFi Connection failed - remove credentials from disk
        self.creds.remove()
        # self.command(PLAY, 0, RESET_WIFI)
        return False

    def start(self, reset_wifi=False):
        # turn off station interface to force a reconnect
        self.sta_if.active(False)
        # 删除wifi密码， 重新连接网络
        if not self.try_connect_from_file():
            self.captive_portal()

    def scan_ssid(self):
        self.sta_if.active(True)
        ssid_list = self.sta_if.scan()
        ssid_list.sort(key=lambda wifi: wifi[3], reverse=True)
        self.sta_if.active(False)
        return ssid_list
