import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class Motor:

    def __init__(self, pin1, pin2, pinControl, my_pwm ):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pin1 = pin1
        self.pin2 = pin2
        self.pinControl = pinControl

        print('Motor __init__  | pin1: ' + str(self.pin1) + ', pin2: ' + str(self.pin2) + ', pinControl:' + str(pinControl) )

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)

        self.pwm_control = GPIO.PWM(self.pinControl, my_pwm )
        self.pwm_control.start(0)

    def forward(self, speed):

        print('Forward  | pin1: ' + str(self.pin1) + ', pin2: ' + str(self.pin2) + ', speed:' + str(speed) )

        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)
        self.pwm_control.ChangeDutyCycle(speed)

    def backward(self, speed):

        print('Backward | pin1: ' + str(self.pin1) + ', pin2: ' + str(self.pin2) + ', speed:' + str(speed) )

        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)
        self.pwm_control.ChangeDutyCycle(speed)


    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
        self.pwm_control.ChangeDutyCycle(0)


GPIO.cleanup()
