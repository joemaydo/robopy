import motor
import time
import Adafruit_PCA9685


class MotorController:

"""er zweite wichtige Befehl ist jener, mit dem wir den Puls für einen angeschlossenen Servo Motor senden. Der
erste Parameter ist dabei der Channel (zw. 0 und 15), der zweite und dritte Parameter ist die relative Pulslänge im
Verhältnis zu 4096 (was 2^12 entspricht). Die Differenz der beiden Werte darf nicht größer als 4096 sein.
Um den Motor in Stellung zu bringen können wir bspw. folgendes eingeben:

pwm.set_pwm(0, 0, 150)

Dabei wird lediglich die Differenz berechnet. Der obige Aufruf ist also äquivalent zu diesem:

pwm.set_pwm(0, 600, 750)

Das Signal wird im folgend berechnet: Möchtest du ein Signal von bspw. 0.5ms (=0.0005s) bei einer Frequenz von 50Hz
(ein Puls ist 20ms breit) ausgeben, so müsste der relative Wert ~100 sein (50Hz * 0.0005s * 4096 = 102.4).
Die üblichen Pulslängen von Servos sind 0.5ms (0°) bis 2.5ms (180°). Dazwischen wird interpoliert.

Wie auch im Beispiel des einfachen Servos gilt, dass wir das „Ruckeln“ des Servos ausstellen können,
sofern wir den Puls auf Null setzen:

pwm.set_pwm(0, 0, 0)

 """


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
