from time import sleep

import RPi.GPIO as GPIO
import pigpio

import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)
pi = pigpio.pi()
pi.set_mode(10, pigpio.OUTPUT)

while True:
    result = instance.read()
    if result.is_valid():
        if result.humidity >= 50:
            pi.write(10, 1)
            sleep(0.5)
            pi.write(10, 0)
            sleep(0.5)
            print("over" + str(result.humidity - 50))

        print("気温：" + str(result.temperature) + "度 " + "湿度：" + str(result.humidity) + "%")
        sleep(1)
