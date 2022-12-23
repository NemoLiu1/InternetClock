from captive_portal import CaptivePortal
import gc

portal = CaptivePortal("Internet_Clock")
portal.start()
gc.collect()
print('ok')
