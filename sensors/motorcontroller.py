import motor
import time
import Adafruit_PCA9685


class MotorController:

    def __init__(self, address=0x40, freq=50):
        self.address = address
        self.pwm = Adafruit_PCA9685.PCA9685(address)
        self.pwm.set_pwm_freq(freq)

    def move(self, direction, speed):
        pass

    def move_forward(self, motor, speed):
        pass

    def move_back(self, motor, speed):
        pass
