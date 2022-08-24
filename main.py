from machine import Pin
from neopixel import NeoPixel
import time

font = [[[1, 1, 1],  # 0
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
         [1, 1, 1]],]

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

def light_on(x, y, red, green, blue):
    location = translate(x, y)
    np[location] = (red , green, blue)
    np.write()

def translate(x, y):
    location = -1
    if x % 2 == 0:
        location = 8 * x + y
    elif x % 2 == 1:
        location = (8 - (y + 1)) + 8 * x
    if location == 0 or location > 256:
        return -1
    return location

# def words(x, y, location):
#     f = font[location]
#         for row in range(len(f)):
#             for col in range(len(f[row])):
#
# # #             if font[row][col]==1:
# # #                 light_on(x+col,y+row)

light_on(3, 5, 50, 0, 0)
