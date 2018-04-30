from time import sleep

import RPi.GPIO as GPIO

from temp_humi import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # BOARDにするとピン番号指定になる
GPIO.cleanup()

# read data using pin 7
instance = dht11.DHT11(pin=7)
GPIO.setup(19, GPIO.OUT)

while True:
    result = instance.read()
    if result.is_valid():
        if result.temperature <= 20:
            GPIO.output(19, True)
            sleep(0.5)
            GPIO.output(19, False)
            sleep(0.5)
            print("over" + str(result.humidity - 50))

        print("気温：" + str(result.temperature) + "度 " + "湿度：" + str(result.humidity) + "%")
        sleep(1)
