#!/usr/bin/python3

import RPi.GPIO as GPIO
import robopy.controller.motorcontroller as motor


EnableLeft = 13
EnableRight = 15
InputLeft1 = 29
InputLeft2 = 31
InputRight3 = 33
InputRight4 = 35

leftMotor = 0
rightMotor = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(EnableLeft, GPIO.OUT)
GPIO.setup(EnableRight, GPIO.OUT)
GPIO.setup(InputLeft1, GPIO.OUT)
GPIO.setup(InputLeft2, GPIO.OUT)
GPIO.setup(InputRight3, GPIO.OUT)
GPIO.setup(InputRight4, GPIO.OUT)

motor = motor.MotorController(InputLeft1, InputLeft2, InputRight3, InputRight4)

motor.set_speed(leftMotor, 0.5)
motor.set_speed(rightMotor, 0.5)


def mainloop():
    while True:
        pass


if __name__ == "__main__":
    mainloop()
