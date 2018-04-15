from time import sleep
import pigpio

while True:
    pi = pigpio.pi()
    pi.set_mode(18, pigpio.OUTPUT)
    pi.write(18, 1)
    sleep(0.05)
    pi.write(18, 0)
    sleep(0.05)