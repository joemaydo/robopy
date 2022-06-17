#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)

EnableLeft = 13
EnableRight = 15
InputLeft1 = 29
InputLeft2 = 31
InputRight3 = 33
InputRight4 = 35

GPIO.setmode(EnableLeft, GPIO.OUT)
GPIO.setmode(EnableRight, GPIO.OUT)
GPIO.setmode(InputLeft1, GPIO.OUT)
GPIO.setmode(InputLeft2, GPIO.OUT)
GPIO.setmode(InputRight3, GPIO.OUT)
GPIO.setmode(InputRight4, GPIO.OUT)

pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)




