from machine import Pin
from neopixel import NeoPixel
import time
from machine import Timer
from captive_portal import CaptivePortal
from dfplayermini import Player
import gc
import ntptime
from machine import RTC

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
Screen_pin = Pin(2, Pin.OUT)
# create a screen(NeoPixel driver) on i/o 19 with 256 pixels
np = NeoPixel(Screen_pin, 256)
# set i/o in to output mode
rtc = RTC()
TIME = 0
DATE = 1
BALL = 2
state = TIME
music = Player(pin_TX=0, pin_RX=1)
t = 0.02
x = -2
y = -1
velocity_y = 0
velocity_x = 1 / 0.02
gravity = 6


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

#
def clean():
    for i in range(0, 256):
        np[i] = (0, 0, 0)


def show():
    np.write()


def light_on(x, y, color=(50, 50, 50)):
    location = translate(x, y)
    if location == -1:
        return
    np[location] = color
    # np.write()

# 根据使用者给出的x与y坐标，通过下面几行将其映射到最终的对应位置。
# 对应位置是一个从0到255的数字，对应的是屏幕上LED灯的序号。
# 如果给出的坐标超过范围将返回-1。
def translate(x, y):
    location = -1
    # 下面是偶数列的映射规则
    if x % 2 == 0:
        location = 8 * x + y
    # 下面是奇数列的映射规则
    elif x % 2 == 1:
        location = (8 - (y + 1)) + 8 * x
    # 判断x与y坐标是否超出范围
    if location == 0 or location > 256:
        # 假如超出范围就会返回一个-1的值
        return -1
    return location


def show_digi(x, y, digital, color=(50, 50, 50)):
    word = font[digital]
    for row in range(0, len(word)):
        for col in range(0, len(word[row])):
            if word[row][col] == 1:
                light_on(x + col, y + row, color)


def print_text(text, x, y):
    for character in text:
        # ord是用于找到该字符对应的Unicode编码
        # 减去46是用来找到该字符在Font里的位置
        character = ord(character) - 46
        word = font[character][0]
        x_axis_len = len(word)
        show_digi(x, y, character)
        x = x + x_axis_len + 1
        # np.write()


def clock_init(timer=None):
    try:
        clean()
        print_text('SYNCING', x=1, y=1)
        show()
        print('Init clock time.')
        ntptime.settime()
        timer.init(period=1000 * 60 * 60, mode=Timer.PERIODIC, callback=sync_time)
        print('Init process successful!')
        # The main reason that I have put the secound timer there(as you can see bellow).
        # Is because in this way, the second timer will not show up before the whole init process is finish,
        # which is a bit odd to happen logically.
        screen_refresh.init(period=30, mode=Timer.PERIODIC, callback=show_time)
    except:
        print('Failed init clock time.')
        print('Trying again after 1 second.')
        timer.init(period=1000, mode=Timer.ONE_SHOT, callback=clock_init)


# padding = 填充
def padding(num):
    if num < 10:
        return '0' + str(num)
    return str(num)


def sync_time(timer=None):
    try:
        print('Syncing UTC+8 time.')
        ntptime.settime()
        print('Sync process successful!')
    except:
        print('Sync time fail.\n Trying again after 1 hour.')

previous_min = 5

def show_time(timer=None):
    global x, y, velocity_y, state, previous_min
    clean()
    current_time = rtc.datetime()
    month  = current_time[1]
    day    = current_time[2]
    hour   = current_time[4]
    minute = current_time[5]
    second = current_time[6]
    # when current_time[5] = 0 (current min) and previous_min = 59, play music
    # 前一时刻的分钟是59，当前时刻的分钟是0的时候，播放整点报时
    if minute == 0 and previous_min == 59 and 7 <= hour <= 22:
        tell_the_time()
    # record the current time in to a variable named “previous_min”.
    # it will be used in the next time to compare the time.
    previous_min = minute
    if state == TIME:
        h = padding(hour)
        m = padding(minute)
        s = padding(second)
        time = h + ':' + m + ':' + s
        print_text(time, 2, 1)
        show()
    elif state == DATE:
        m = padding(month)
        d = padding(day)
        time = m + "/" + d
        print_text(time, 6, 1)
        show()
    elif state == BALL:
        displacement = velocity_y * t + gravity * t * t / 2
        velocity_y = gravity * t + velocity_y
        y = y + displacement * 200
        x = velocity_x * t + x
        light_on(int(x), int(y))
        show()
        print(x, y, displacement, velocity_y, velocity_x)
        if y > 8:
            velocity_y = -velocity_y * 0.7
            y = 7.9

        if x >= 33:
            state = TIME


def date_time_button_handler(pin):
    global state
    if state == TIME:
        state = DATE
        print('screen state = 1')
    elif state == DATE:
        state = TIME
        print('screen state = 0')


def sound_button_handler(pin):
    print('sound button triggered')
    tell_the_time()

def ball_button_handler(pin):
    global x, y, velocity_y, state
    state = BALL
    x = 0
    y = 0
    velocity_y = 0

def tell_the_time():
    print('telling the time.')
    current_time = rtc.datetime()
    hour = current_time[4]
    minute = current_time[5]
    music.play(hour + 1)
    if minute == 0:
        return
    time.sleep_ms(1400)
    music.play(minute + 25)

clean()
print_text('WIFI...', 1, 1)
show()

portal = CaptivePortal("Internet_Clock")
portal.start()
gc.collect()
print('ok')

ntptime.NTP_DELTA = 3155644800
ntptime.host = 'pool.ntp.org'

# system timer

clock_timer = Timer(0)
clock_timer.init(period=500, mode=Timer.ONE_SHOT, callback=clock_init)

screen_refresh = Timer(2)

# +-
# dfplayer


# screen state handler/controller

date_button = Pin(6, Pin.IN)
ball_button = Pin(4, Pin.IN)
sound_track = Pin(8, Pin.IN)
date_button.irq(handler=date_time_button_handler, trigger=Pin.IRQ_RISING)
sound_track.irq(handler=sound_button_handler, trigger=Pin.IRQ_RISING)
ball_button.irq(handler=ball_button_handler, trigger=Pin.IRQ_RISING)
