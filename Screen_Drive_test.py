from machine import Pin
from neopixel import NeoPixel

Screen_pin = Pin(2, Pin.OUT)
np = NeoPixel(Screen_pin, 256)

def light_on(x, y, color=(50, 50, 50)):
    location = translate(x, y)
    if location == -1:
        return
    np[location] = color


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

light_on(1, 1)
light_on(1,2,color=(50,100,50))
np.write()
