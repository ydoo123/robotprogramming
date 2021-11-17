import modi
import time
import os

bundle = modi.MODI()
print(bundle.modules)

speaker = bundle.speakers[0]
speaker.tune = 3591, 50

time.sleep(2)

speaker.frequency = 1975
time.sleep(2)

speaker.volume = 100
time.sleep(2)

speaker.turn_off()
os.system("pause")

