
import motor
import time
import Adafruit_PCA9685


def get_servo_pulse(pulse):
    pulse_length = 1000000
    pulse_length //= 60
    pulse_length //= 4096
    pulse *= 1000
    pulse //= pulse_length
    return pulse


class MotorController:

    pwm_pulse = 4096

    def __init__(self, leftMotor: motor, rightMotor: motor, channel_left=0, channel_right=1, address=0x40, freq=50):
        self.address = address
        self.freq = freq
        self.pwm = Adafruit_PCA9685.PCA9685(address)
        self.pwm.set_pwm_freq(freq)
        self.channel_left = channel_left
        self.channel_right = channel_right

        self.leftMotor = leftMotor
        self.rightMotor = rightMotor

    def move_forward(self, engine: motor, pwm_channel, speed: float):
        pass

    def move_back(self, engine: motor, speed):
        pass

    def move_left(self, engine, speed):
        pass

    def move_right(self, engine, speed):
        pass

    def move(self, speed: float, pwm_channel):
        speed = int(speed * self.pwm_pulse)
        self.pwm.set_pwm(pwm_channel, 0, speed)
