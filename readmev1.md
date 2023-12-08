# Internet Clock

### ! Attention:

### The author have only programmed this program through with a windows 11 operating system.  There might be mistakes and place that won't work out for you, you might need to adapt to some of the changes by yourself.

## Project's initial

#### How dose I can out this idea

The whole thing started when a day in the June, my mom complained about the clock we got in the center of the room was not working all the time, and when ever she is reseating up the clock, by changing battery, she needs to do the readjusting time process (adjust it to the current time).Which inspired me with an idea, that to have a clock with no need of setting up process since the first time it start working. Although the idea of spending serval days working on this project just to fix this problem seems dumb,  but actually it turns out all the effort are worth. This idea has also been promoted, when I heard about personal project. Because I have this project on the line and the idea of making a clock on the other side, so I decided this clock, is going to be my project that I will be working on in the rest of the year.

#### Why is this a problem?

In a normal situation, clock have errors with time. Even though keep the time in track is purpose of the clock, but in the most case errors do exist. After a few month or so, it will need a adjustment on the time. It can be freak people out if it happens. So, after we find a problem, then we need to find a way to fix it. That is where me and the Internet Clock comes in. I want to challenge myself by working on a clock that can preventing other to get this problem. In the process, I will also be learning new knowledge and techniques. It is existing for me. 

#### Previous project about the similar topic, how did they done it and what can we improve.

When I go over this whole thing with my dad, a professional software developer, tries to gets some idea of where should I get this started. He told me that I could try find open sources projects on GitHub, which contains all sorts of developer who shared their own unique projects. So, after I learned a couple of things from my dad, about how should I find information on GitHub. Then I started browsing on GitHub. After a few hours of searching, finally find a project named "AWTRIX1.0" (used "Matrix Clock"  as the key word), with the 113 stars (a system allows user to support author, similar as the "like button" in YouTube). Through "AWTRIX1.0" 's readme.md document, we would know that there is a 2.0 version of this project, for the 1.0 one, it is already outdated. After reading through the 2.0 version we realized that, in his design, he plans to clock able to show the time and keep the time updated, also provided the function of allowing it's user to create unique function and share it with other user. On the other hands,  we find out that what was included in this project it way too powerful, and it is also way complicated that what I have imagined. I have listed out the pros and it's difficulties that we don't necessary need in my  project below.

1. Pros

   1. Serial connection or USB connection to the matrix

   2. Gesture sensor for operation (optional)

   3. Temperature and humidity sensor (optional)

   4. Light sensor for brightness control (optional)

2. However these functions came with a restriction

   In his design, he have provided many useful functions that would help and make the screen have more variability. However, we need to setup the host up first. The host is a program that need to be on at the whole time in order to keep the clock(controller) running. Which means, if you want this clock to be on is useable, you should keep your PC or what ever device you got the host on on the  whole time. 

So, after discussion with my dad about the details of the personal project, he suggest me to work on a rather smaller and simpler project than this one. I listen what he recommended, then approached my own project according to AWTRIX's hardware. I named it -- Internet Clock. After a time of thinking, I have **seted** up 3 goals.

First, my clock should be able to auto sync the time by using connection with a NTP server. Which is a server runs exsac time.

Second, it should be able to call out time during each hour (in the range of 7 am  in the morning to 22 pm in the night).'

Third, it should be able to show the exact time of the day by using WS2812 matrix screen, in a fine order for people to read and identify the time.

After Listed out our goal and expectation for internet clock. It time to come up with a plan.

![image-20221217223634671](images/image-20221217223634671.png)

## Project start

### Prototype

#### Purpose of Prototype

Through the process of building up a simple prototype, to see the prototype with the cooperate with software we got is it able to achieve our goal. 

#### Purchase Component

List of Component

| id   |  Component's Name(name in the passage)   |      Used for       | Amount used |
| ---- | :--------------------------------------: | :-----------------: | :---------: |
| 01   |         LUATOS ESP32-c3 (esp32)          |  micro controller   |      1      |
| 02   |         DFPlayer mini(DF player)         |     sound model     |      1      |
| 03   |          Micro SD card(TF card)          | sound track restore |      1      |
| 04   | TTP223 touch button model (touch button) |    touch button     |      3      |
| 05   |       Speaker (4ohm 3w) (speaker)        |     play sound      |      1      |
| 06   | WS2812 Matrix Screen (8*32 pix) (screen) |    display time     |      1      |

(all the hardwire component above are bought from Taobao)

#### Installation of Micropython Firmware

In order to get started with micropython on the "esp32" main bord, you would have to install and set up the basis for our future programming. Here are the steps: 

1. Download and setup python (done before hands)

2. Use "pip" command in python, to get download "esptool".

3. Gide yourself to the website "https://micropython.org/download/esp32c3/".

4. Download the most resent update for the firmware (I used v1.19.1(2022-06-18).bin).

5. Before cleaning up the date that was left in "esp32" by the compony, you need to looked up which port it is using.

   1. right click "my computer" find the "menage" option in context menu.

   2. now you should able to see a list of stuff under "computer manager (loco)", find "device manager" -> "port".

   3. Pulge in the device(esp32), you should be able to see the fight device poped up on your screen, at the end of the list of words, there is the right Port.

      ![image-20221203230028563](images\image-20221203230028563.png)

   4. Remember the port for you (mine is COM4).

6. After getting the port, you should open up windows terminal.

7. Make sure your device is connect to your computer, then enter this command (remember to enter the right port for you):

   ```bash
   esptool.py --chip esp32c3 --port com4 erase_flash
   ```

8. When it is successfully done, you would find some thing similar with this:

   ```text
   esptool.py v3.0
   Serial port com4
   Connecting....
   WARNING: This chip doesn't appear to be a ESP32-C3 (chip magic value 0x1b31506f). Probably it is unsupported by this version of esptool.
   Chip is unknown ESP32-C3
   Features: Wi-Fi
   Crystal is 40MHz
   MAC: 60:55:f9:7e:5f:b0
   Uploading stub...
   Running stub...
   Stub running...
   Erasing flash (this may take a while)...
   Chip erase completed successfully in 0.0s
   Hard resetting via RTS pin...
   ```

9. Now congratulation :) , you have successfully delete what ever was left in the chip, now is time for you to setup the firmware. 

10. Reminder, plz make sure you have done step 4 already. Enter:

    ```bash
    esptool.py --chip esp32c3 --port com4 --baud 460800 write_flash -z 0x0 esp32c3-20220117-v1.18.bin
    ```

11. You should be expecting following masage to shown you are correct:

    ```text
    esptool.py v3.0
    Serial port com4
    Connecting....
    WARNING: This chip doesn't appear to be a ESP32-C3 (chip magic value 0x1b31506f). Probably it is unsupported by this version of esptool.
    Chip is unknown ESP32-C3
    Features: Wi-Fi
    Crystal is 40MHz
    MAC: 60:55:f9:7e:5f:b0
    Uploading stub...
    Running stub...
    Stub running...
    Changing baud rate to 460800
    Changed.
    Configuring flash size...
    Compressed 1437472 bytes to 872137...
    Wrote 1437472 bytes (872137 compressed) at 0x00000000 in 20.7 seconds (effective 554.8 kbit/s)...
    Hash of data verified.
    
    Leaving...
    Hard resetting via RTS pin...
    ```

##### Firmware test 

After we have successfully install the firmware, how should we know does it work or not. That is the question we got after we installed the firmware. After reading the document from official  micropython website, we find out they have provided a tool named mpremote (a.k.a MicroPython remote control) that is able to let use login  MCU console. In this way, we can used the way of directly run a simple program to test out the question of does firmware work or not. (link are at the bottom of this section)

1. via pip to install mpremote, through this command in windows terminal.

   ```sh
   $ pip install mpremote
   ```

2. After the instalation, things are simplar. You can directly type "mpremote" and then enter.

   ```sh
   mpremote
   ```

   It should response massage.

   ```sh
   Connected to MicroPython at COM4
   Use Ctrl-] to exit this shell
   ```

   Now click enter again to get in to the position. (You should able to the python prompt)

   ```sh
   
   >>>
   ```

3. Let it print hello world, to see does it work or not.

   ```python
   >>> print('Hello World')
   Hello Would
   ```

4. If you are able to see the feedback word sine said Hello Would , like the e.g. bellow, that means you have successfully downloaded the mpremote.

   ```python
   Hello Would
   ```

   

[micropython docummant website]: https://docs.micropython.org/en/latest/
[mpremote explanation page]: https://docs.micropython.org/en/latest/reference/mpremote.html#





Use pip to install MicroPython remote control (mpremote).

#### WS2812 Matrix test

What is WS2812 Matrix?

WS2812 Matrix is a screen made up of 256 LED light, which is lined up in the zigzag order. You can see a more sepcific sample of it bellow. This Matrix screen also have the benefit of able to use with the limited of only one GPIO.

Follow the image down bellow, you can connect Matrix screen with ESP32 MCU.

| ESP32-c3 MCU | WS2812 Matrix Screen |
| ------------ | -------------------- |
| Pin32 GND    | GND                  |
| Pin31 5V     | VCC                  |
| Pin19 GPIO02 | DIN                  |

![817b03e9a23c92eaf153790a735b679](images/817b03e9a23c92eaf153790a735b679.png)



Use Micropython to control the screen. 

In this test, I want to make sure all the light bulb is available for all colour, at the same time, try out ways to actually control the secreen.

In order to make sure the LED light do work in all colour, I have picked a relitivaly while colour as the test colour because in a simple screen like this one, it normally use 3 primory colour to immatate the w

需要更多细节

```python
from machine import Pin
from neopixel import NeoPixel
import time
# screen section

# this is a basic command to light up one pic by another with the speed of 10ms per light on on the screen

# set i/o in to output mode
Screen_pin = Pin(2, Pin.OUT)
# create a screen(NeoPixel driver) on i/o 19 with 256 pixels
np = NeoPixel(Screen_pin, 256)

# a test tool that can light up each pixel one by one.
for i in range(256):
    # set all the color to (50, 50 ,50) in the order of rgb.
    np[i] = (50, 50, 50)
    # actally write all the date on the pixels, intuitively, it will light up your screen.
    np.write()
    # delay for 10ms
    time.sleep_ms(10)
```



#### DFPlayer Mini test

What is DFPlayer Mini?

The DFPlayer Mini is a sound model, specifically designed for sound track playing. In this statuation, I'm planning on use DFPlayer Mini and MCU to help my clock be able to tell the time and play out interesting sound. (more information if need, see the official website link at the end of this section)

Follow the image bellow to connect the model with MCU.

| ESP32-c3 MCU  | DFPlayer Mini model   | Speaker |
| ------------- | --------------------- | ------- |
| Pin02 UART_TX | RX (with 1k resistor) | -       |
| Pin03 UART_RX | TX (with 1k resistor) | -       |
| Pin16 5V      | VCC                   | -       |
| Pin14 GND     | GND                   | -       |
| -             | SPK_1                 | VCC     |
| -             | SPK_2                 | GND     |

![8e674fec9e5aaec9af83f80aa168e7b](images/8e674fec9e5aaec9af83f80aa168e7b.png)

DFPlayer Mini Test

Before we start with this testing, Micropython haven't provided any driver for this model,. So in order to get it working, we will be needing to download a program for another person. This link down bellow should help you jump to his website directly.

Link: https://github.com/lavron/micropython-dfplayermini

When you are in this site, you should be finding a program named “dfplayermini.py”. In this program, he have written a drive to control this model.

After this, follow the process bellow to test the sound model.

Put a track of mp3 in the TF card, this is the track that you will be using for testing.

After plug in the TF card, run this program. It should be able to run the first mp3 track that you have put in.

```python
from dfplayermini import Player

music = Player(pin_TX=0, pin_RX=1)
music.play(1)
```



https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299



#### Touch button test

## Hardware

#### Draw PCB

When we have done prototype, and combin all the models and stuff together. I realized a serious problem.

![6d5dd1a44b4364fc4cf229f4dac5436](images/6d5dd1a44b4364fc4cf229f4dac5436.jpg)

This thing is incredibly unorganized. 

PCB is a better solution when we come the final product. PCB board connects all the component of a project together, without having the DuPont wires around. 

In this project, I used 嘉立创EDA. A free software power by Chinese compony. It is useful when coming to design the PCB board.

The image shown bellow is the electrical schematic.

![28536302d940283b807aa3840641e72](images/28536302d940283b807aa3840641e72.png)

![71098472800541a215235825ecbf213](images/71098472800541a215235825ecbf213.png)





#### Proofing PCB

Here, thanks for the comany, as they have willing to do this board for free.

The process will take a while, so at this point I'm able to do work on the software parts,

#### Soldering

After days of waiting, finally the PCB arrived. Right before the soldering, I have taken a picture of all the martials.

![3e9f9d0ce6ba6b9d928049a7162d382](images/3e9f9d0ce6ba6b9d928049a7162d382.jpg)







## Software

#### Drive the Screen

All the things we have done by now, is only a small present of the job. Software is the actual thing. In this portion, we will be writing a system that helps to organize the text you have put in.

In the WS2812 Matrix screen, the way they arranged the LED light is different with how we normally do. In a 2D surface, we normally will convey the position of a point by using x and y, however, in this satiation, the position of the light are arraigned in a zigzag order, which is hard for us to know where is the position of the LED light and convey the position with the computer. So, I came up with the idea of having a method named "translate", it's job is to convert the x and y, we typed in, into the right LED number in the Matrix screen.

This is what I have done. 

```python
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
    # Bellow is the rules applied for even number columns.
    if x % 2 == 0:
        location = 8 * x + y
    # Bellow is the rules applied for odd number columns.
    elif x % 2 == 1:
        location = (8 - (y + 1)) + 8 * x
    # Evaluate is it the coordinate out of bounce.
    if location == 0 or location > 256:
        # If it is out of bounce, it will returen the value -1.
        return -1
    return location

light_on(1, 1)
light_on(1,2,color=(50,100,50))
np.write()
```

![cc3a4cb3805dfd3221e07d3e126fc16](images/cc3a4cb3805dfd3221e07d3e126fc16.jpg)

This is how it look after I have run the test.

After bulling a single light on the screen, now it is time to try to get word on it.

In this process, we made our font collection with the reference form internet. Especially based on this one.

![7e2d13c0fc12f3664977093adba0a13](images/7e2d13c0fc12f3664977093adba0a13.png)

Thanks the support from txigreman. Here is the direct link to the site.

[Font site]: https://fontstruct.com/fontstructions/show/1618858/pixel-5x3-2

According to this, I made my font array. But It takes up too many place, you can refer the my full program on GitHub. 

```python
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
        # refer more info on my GitHub
        ...
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
        ]

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

def show():
    np.write()

print_text('HELLO',0,1)
show()

```

![f55c99e2e914a0cff15e6031b3b05ad](images/f55c99e2e914a0cff15e6031b3b05ad.jpg)



#### Connect to Internet & Sync time

The process of connecting to the internet, keep it stable and usable is rather hard, so again, my solution here is to use other's work from GitHub. Here a special thanks to Anson-VanDoren. In this work 'esp8266-captive-portal', he have created a program that helps MCU to connect the internet through the process of remembering the WIFI password after you have enter the password by your phone the first time. 

[captive portal]: https://github.com/anson-vandoren/esp8266-captive-portal

```python
from captive_portal import CaptivePortal
import gc

portal = CaptivePortal("Internet_Clock")
portal.start()
gc.collect()
print('ok')
```

You should be able to see the text feedback of "ok" from MCU. (NOT from screen)

Now we are done with connect to internet, it is time to go further, sync time form NTP server.

In this process, I have realized there are uncertainties that might cost the process of connect to internet fail. So, in order to prevent if the clock can't connect to internet, I have designed it will not stop, and keep trying to connect of it is not.

```python
import ntptime
from machine import Timer

ntptime.NTP_DELTA = 3155644800
ntptime.host = 'pool.ntp.org'

# system timer
def clock_init(timer=None):
    try:
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

clock_timer = Timer(0)
clock_timer.init(period=500, mode=Timer.ONE_SHOT, callback=clock_init)
```



#### Tell the time

In this section, I have two main parts, show the time live on screen, and play out the time through speaker.



```python
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
        # refer more info on my GitHub
        ...
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
        ]

Screen_pin = Pin(2, Pin.OUT)
np = NeoPixel(Screen_pin, 256)
rtc = RTC()
TIME = 0
DATE = 1
BALL = 2
state = TIME
music = Player(pin_TX=0, pin_RX=1)

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

def translate(x, y):
    location = -1
    if x % 2 == 0:
        location = 8 * x + y
    elif x % 2 == 1:
        location = (8 - (y + 1)) + 8 * x
    if location == 0 or location > 256:
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
        character = ord(character) - 46
        word = font[character][0]
        x_axis_len = len(word)
        show_digi(x, y, character)
        x = x + x_axis_len + 1

def clock_init(timer=None):
    try:
        clean()
        print_text('SYNCING', x=1, y=1)
        show()
        print('Init clock time.')
        ntptime.settime()
        timer.init(period=1000 * 60 * 60, mode=Timer.PERIODIC, callback=sync_time)
        print('Init process successful!')
        screen_refresh.init(period=30, mode=Timer.PERIODIC, callback=show_time)
    except:
        print('Failed init clock time.')
        print('Trying again after 1 second.')
        timer.init(period=1000, mode=Timer.ONE_SHOT, callback=clock_init)

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
    if minute == 0 and previous_min == 59 and 7 <= hour <= 22:
        tell_the_time()
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

clock_timer = Timer(0)
clock_timer.init(period=500, mode=Timer.ONE_SHOT, callback=clock_init)

screen_refresh = Timer(2)
```







#### Button function and easter egg





## Case

#### Lay out & Designs



#### Build up







Difficulties I have encountered during the way & how did I face and fix it. 





#### PCB Testing & Debug



## Credit for

I have used some of other people's work on the way or in this project, so I will list it out:



I would like to give credit for the list of people, with out them, this project will not be possible.










