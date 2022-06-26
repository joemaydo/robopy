import l298n
import time
import Adafruit_PCA9685
import numpy as np


def get_servo_pulse(pulse: int) -> int:
    pulse_length = 1000000
    pulse_length //= 60
    pulse_length //= 4096
    pulse *= 1000
    pulse //= pulse_length
    return pulse


class MotorController:

    __pwm_pulse = 4096

    def __init__(self, pin_left_1, pin_left_2, pin_right_1, pin_right_2, address=0x40, freq=50):
        self.__address = address
        self.__freq = freq
        self.__pwm = Adafruit_PCA9685.PCA9685(address)
        self.__pwm.set_pwm_freq(freq)
        self.__motorLeft = l298n(pin_left_1, pin_left_2)
        self.__motorRight = l298n(pin_right_1, pin_right_2)

        self.__motor_speed = [0, 0]

    def move_forward(self, engine: l298n, pwm_channel, speed: float):
        pass

    def move_back(self, engine: l298n, speed):
        pass

    def move_left(self, engine, speed):
        pass

    def move_right(self, engine, speed):
        pass

    def move(self, speed: float, pwm_channel):
        speed = int(speed * self.__pwm_pulse)
        self.__pwm.set_pwm(pwm_channel, 0, speed)

    def get_speed(self, channel):
        return self.__motor_speed[channel]

    def set_speed(self, channel, speed):
        self.__motor_speed[channel] = speed

