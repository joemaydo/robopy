#!/usr/bin/python3


import RPi.GPIO as GPIO
import sys


pinLed = 11
ledOn = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLed, GPIO.OUT)


def change_led(value):
    if value == 'y':
        GPIO.output(pinLed, True)
        print("Led is on")
    elif value == 'n':
        GPIO.output(pinLed, False)
        print("Led is off")
    else:
        GPIO.output(pinLed, False)
        print("Led is off")


while True:
    try:
        inputValue = input("y oder n für Led wechsel")
        change_led(inputValue)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

