from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(7, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 1)  # ブザーの設定

try:
    while True:
        if GPIO.input(7) == GPIO.HIGH:  # スイッチが押されているなら
            p.start(50)
            p.ChangeFrequency(262)
        else:
            p.stop()
        sleep(0.01)

except:
    pass

GPIO.cleanup()
