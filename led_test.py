import modi
import os
import time

bundle = modi.MODI()
led = bundle.leds[0]
led.rgb = 100, 100, 100
led.turn_on()
time.sleep(2)

led.turn_off()
