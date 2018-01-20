import threading
import time

import RPi.GPIO as GPIO
# GPIO = RPi.GPIO
#
# import pigpio
# pi = pigpio.pi() # Connect to local Pi.


MOTOR1_PIN  = 23
MOTOR2_PIN  = 5

SERVO_H_PIN  = 26
SERVO_V_PIN  = 20

class PiThing(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        # Setup GPIO library.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Setup LED as an output and switch as an input.
        GPIO.setup(MOTOR1_PIN, GPIO.OUT)
        GPIO.setup(MOTOR2_PIN, GPIO.OUT)

        GPIO.setup(SERVO_H_PIN, GPIO.OUT)
        GPIO.setup(SERVO_V_PIN, GPIO.OUT)

        self.pwm_h = GPIO.PWM(SERVO_H_PIN, 50)
        self.pwm_h.start(6.5)

        self.pwm_v = GPIO.PWM(SERVO_V_PIN, 50)
        self.pwm_v.start(6.5)

        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def view_up(self, value):
        with self._lock:
            print "up"
            self.pwm_h.ChangeDutyCycle(3.5)
            #GPIO.cleanup()
            time.sleep(1)
            # self.pwm_h.stop()

    def view_down(self, value):
        with self._lock:
            print "down"
            self.pwm_h.ChangeDutyCycle(7.5)
            #GPIO.cleanup()
            # time.sleep(1)
            # self.pwm_h.stop()

    def view_left(self, value):
        with self._lock:
            self.pwm_v.ChangeDutyCycle(9.5)

    def view_right(self, value):
        with self._lock:
            self.pwm_v.ChangeDutyCycle(3.5)

    def read_switch(self):
        with self._lock:
            return GPIO.input(MOTOR1_PIN)

    def direction_forward(self, value):
        print value
        with self._lock:
            GPIO.output(MOTOR1_PIN, value)
            GPIO.output(MOTOR2_PIN, value)

    def direction_backward(self, value):
        print value
        with self._lock:
            GPIO.output(MOTOR1_PIN, value)
            GPIO.output(MOTOR2_PIN, value)

    def direction_left(self, value1, value2):
        with self._lock:
            GPIO.output(MOTOR1_PIN, value1)
            GPIO.output(MOTOR2_PIN, value2)

    def direction_right(self, value1, value2):
        with self._lock:
            GPIO.output(MOTOR1_PIN, value1)
            GPIO.output(MOTOR2_PIN, value2)

    def direction_stop(self, value):
        print value
        with self._lock:
            GPIO.output(MOTOR1_PIN, value)
            GPIO.output(MOTOR2_PIN, value)
