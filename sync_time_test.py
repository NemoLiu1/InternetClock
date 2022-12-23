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

