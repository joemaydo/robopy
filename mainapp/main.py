#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
import controller.motorcontroller as motor


GPIO.setmode(GPIO.BCM)

EnableLeft = 13
EnableRight = 15
InputLeft1 = 29
InputLeft2 = 31
InputRight3 = 33
InputRight4 = 35

leftMotor = 0
rightMotor = 1

GPIO.setmode(EnableLeft, GPIO.OUT)
GPIO.setmode(EnableRight, GPIO.OUT)
GPIO.setmode(InputLeft1, GPIO.OUT)
GPIO.setmode(InputLeft2, GPIO.OUT)
GPIO.setmode(InputRight3, GPIO.OUT)
GPIO.setmode(InputRight4, GPIO.OUT)

motor = motor.MotorController(InputLeft1, InputLeft2, InputRight3, InputRight4)

motor.set_speed(leftMotor, 0.5)
motor.set_speed(rightMotor, 0.5)


def mainloop():
    while True:
        pass


if __name__ == "__main__":
    mainloop()





