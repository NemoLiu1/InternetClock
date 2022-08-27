from machine import Pin
from neopixel import NeoPixel
import time
from machine import Timer
from captive_portal import CaptivePortal
from dfplayermini import Player
import gc
import ntptime

font = [[[0],  # .
         [0],
         [0],
         [0],
         [1]],
        [[0, 0, 1],  # /
         [0, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [1, 0, 0]],
        [[1, 1, 1],  # 0
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]],
        [[0, 1, 0],  # 1
         [1, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],
        [[1, 1, 0],  # 2
         [0, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [1, 1, 1]],
        [[1, 1, 0],  # 3
         [0, 0, 1],
         [0, 1, 1],
         [0, 0, 1],
         [1, 1, 0]],
        [[1, 0, 1],  # 4
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [0, 0, 1]],
        [[1, 1, 1],  # 5
         [1, 0, 0],
         [1, 1, 0],
         [0, 0, 1],
         [1, 1, 0]],
        [[1, 1, 1],  # 6
         [1, 0, 0],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],
        [[1, 1, 1],  # 7
         [0, 0, 1],
         [0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
        [[1, 1, 1],  # 8
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],
        [[1, 1, 1],  # 9
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
        [[0],
         [1],  # :
         [0],
         [1],
         [0]],
        [[0],
         [1],  # ;
         [0],
         [1],
         [1]],
        [[0, 0, 1],  # <
         [0, 1, 0],
         [1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]],
        [[0, 0, 0],  # =
         [1, 1, 1],
         [0, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[1, 0, 0],  # >
         [0, 1, 0],
         [0, 0, 1],
         [0, 1, 0],
         [1, 0, 0]],
        [[1, 1, 1],  # ?
         [0, 0, 1],
         [0, 1, 0],
         [0, 0, 0],
         [0, 1, 0]],
        [[0, 1, 0],  # @
         [1, 0, 0],
         [1, 1, 1],
         [1, 0, 1],
         [0, 1, 0]],
        [[0, 1, 0],  # A
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 0, 1]],
        [[1, 1, 0],  # B
         [1, 0, 1],
         [1, 1, 0],
         [1, 0, 1],
         [1, 1, 0]],
        [[0, 1, 1],  # C
         [1, 0, 0],
         [1, 0, 0],
         [1, 0, 0],
         [0, 1, 1]],
        [[1, 1, 0],  # D
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 0]],
        [[1, 1, 1],  # E
         [1, 0, 0],
         [1, 1, 0],
         [1, 0, 0],
         [1, 1, 1]],
        [[1, 1, 1],  # F
         [1, 0, 0],
         [1, 1, 0],
         [1, 0, 0],
         [1, 0, 0]],
        [[0, 1, 1],  # G
         [1, 0, 0],
         [1, 0, 1],
         [1, 0, 1],
         [0, 1, 1]],
        [[1, 0, 1],  # H
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 0, 1]],
        [[1],  # I
         [1],
         [1],
         [1],
         [1]],
        [[1, 1, 1],  # J
         [0, 0, 1],
         [0, 0, 1],
         [1, 0, 1],
         [0, 1, 0]],
        [[1, 0, 1],  # K
         [1, 0, 1],
         [1, 1, 0],
         [1, 0, 1],
         [1, 0, 1]],
        [[1, 0, 0],  # L
         [1, 0, 0],
         [1, 0, 0],
         [1, 0, 0],
         [1, 1, 1]],
        [[1, 0, 1],  # M
         [1, 1, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 0, 1]],
        [[0, 1, 1],  # N
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1]],
        [[1, 1, 1],  # O
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]],
        [[1, 1, 1],  # P
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 0],
         [1, 0, 0]],
        [[1, 1, 1],  # Q
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1],
         [0, 0, 1]],
        [[1, 1, 1],  # R
         [1, 0, 1],
         [1, 1, 0],
         [1, 0, 1],
         [1, 0, 1]],
        [[1, 1, 1],  # S
         [1, 0, 0],
         [1, 1, 1],
         [0, 0, 1],
         [1, 1, 1]],
        [[1, 1, 1],  # T
         [0, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
        [[1, 0, 1],  # U
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [1, 1, 1]],
        [[1, 0, 1],  # v
         [1, 0, 1],
         [1, 0, 1],
         [1, 0, 1],
         [0, 1, 0]],
        [[1, 0, 0, 0, 1],  # W
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 1],
         [1, 0, 0, 0, 1]],
        [[1, 0, 1],  # X
         [1, 0, 1],
         [0, 1, 0],
         [1, 0, 1],
         [1, 0, 1]],
        [[1, 0, 1],  # Y
         [1, 0, 1],
         [1, 1, 1],
         [0, 1, 0],
         [0, 1, 0]],
        [[1, 1, 1],  # Z
         [0, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [1, 1, 1]],
        [[0, 0, 0],  # 3*5 blank
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        [[0, 0, 0, 0],  # 4*5 blank
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        ]

# screen section

# basic comand to light up one pic on the screen
Screen_pin = Pin(19, Pin.OUT)
# create a screen(NeoPixel driver) on i/o 19 with 256 pixels
np = NeoPixel(Screen_pin, 256)
# set i/o in to output mode

# # a test tool that can light up each pixel one by one.
# for i in range(256):
#     np = NeoPixel(Screen_pin, 256)
#     # set all the color to (50, 50 ,50) in the order of rgb.
#     np[i] = (50, 50, 50)
#     # actally write all the date on the pixels, intuitively, it will light up your screen.
#
#     # delay for 10ms
#     time.sleep_ms(10)
#
# np.write()
# font

def clean():
    for i in range(0, 256):
        np[i]=(0,0,0)

def show():
    np.write()

def light_on(x, y, color = (50, 50, 50)):
    location = translate(x, y)
    np[location] = color
    # np.write()

def translate(x, y):
    location = -1
    if x % 2 == 0:
        location = 8 * x + y
    elif x % 2 == 1:
        location = (8 - (y + 1)) + 8 * x
    if location == 0 or location > 256:
        return -1
    return location

def show_digi(x, y, digital = 0, color = (50, 50, 50)):
    word = font[digital]
    for row in range(0, len(word)):
        for col in range(0, len(word[row])):
            if word[row][col] == 1:
                light_on(x + col, y + row, color)

def print_text(x = 1, y = 1, text = 'Hi'):
    for character in text:
        character = ord(character) - 46
        word = font[character][0]
        x_axis_len = len(word)
        show_digi(x, y, character)
        x = x + x_axis_len + 1
        np.write()

def clock_init(timer=None):
    try:
        clean()
        print_text(text = 'SYNCING')
        show()
        print('Init clock time.')
        ntptime.settime()
        timer.init(period=1000 * 60 * 60, mode=Timer.PERIODIC, callback=sync_time)
        print('Init process successful!')
    except:
        print('Failed init clock time.')
        print('Trying again after 1 second.')
        timer.init(period=1000, mode=Timer.ONE_SHOT, callback=clock_init)

def sync_time(timer=None):
    try:
        print('Syncing UTC+8 time.')
        ntptime.settime()
        print('Sync process successful!')
    except:
        print('Sync time fail.\n Trying again after 1 hour.')

# def show_time():
#     rtc = RTC()
#     rtc.datetime()

clean()
print_text(1,1,'WIFI...')
show()

portal = CaptivePortal("Internet_Clock")
portal.start()
gc.collect()
print('ok')

ntptime.NTP_DELTA = 3155644800
ntptime.host = 'pool.ntp.org'

clock_timer = Timer(0)
clock_timer.init(period=500, mode=Timer.ONE_SHOT, callback=clock_init)

# screen_refresh = Timer(2)
# screen_refresh.init(period=20, mode=Timer.PERIODIC, callback=)

# show_digi(1,1,0)
# show_digi(5,1,1)
# show_digi(9,1,2)
# show_digi(13,1,3)
# show_digi(17,1,4)
# show_digi(21,1,5)
# print_text(1, 1, 'NEMO')

# import time
# time.sleep(3)
# spacing(0,0,0)
# spacing(0,0,4)

# light_on(3, 5, (0,0,50))
