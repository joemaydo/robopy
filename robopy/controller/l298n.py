import RPi.GPIO as GPIO


class L298N:

    def __init__(self, pinIN1, pinIN2, setupMode=GPIO.BCM):
        self.__pinIN1 = pinIN1
        self.__pinIN2 = pinIN2
        self.setupMode = setupMode

        GPIO.setmode(setupMode)
        GPIO.setup(pinIN1, GPIO.OUT)
        GPIO.setup(pinIN2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.__pinIN1, GPIO.HIGH)
        GPIO.output(self.__pinIN2, GPIO.LOW)

    def back(self):
        GPIO.output(self.__pinIN1, GPIO.LOW)
        GPIO.output(self.__pinIN2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.__pinIN1, GPIO.LOW)
        GPIO.output(self.__pinIN2, GPIO.LOW)

    def exit(self):
        GPIO.output(self.__pinIN1, GPIO.LOW)
        GPIO.output(self.__pinIN2, GPIO.LOW)
        GPIO.cleanup()
