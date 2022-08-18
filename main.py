from machine import Pin
from neopixel import NeoPixel
import time
# screen section

# basic comand to light up one pic on the screen
# set i/o in to output mode
Screen_pin = Pin(19, Pin.OUT)
# create a screen(NeoPixel driver) on i/o 19 with 256 pixels
np = NeoPixel(Screen_pin, 256)

# a test tool that can light up each pixel one by one.
for i in range(256):
    np = NeoPixel(Screen_pin, 256)
    # set all the color to (50, 50 ,50) in the order of rgb.
    np[i] = (50, 50, 50)
    # actally write all the date on the pixels, intuitively, it will light up your screen.
    np.write()
    # delay for 10ms
    time.sleep_ms(10)

