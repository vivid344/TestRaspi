from time import sleep

import random
import pigpio

# とりあえずGPIO18ピンをLチカ

while True:
    pi = pigpio.pi()
    pi.set_mode(10, pigpio.OUTPUT)
    pi.write(10, 1)
    sleep(random.uniform(0,0.1))
    pi.write(10, 0)
    sleep(random.uniform(0,0.1))
