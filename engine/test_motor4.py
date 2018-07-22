import RPi.GPIO as GPIO
# this imports the GPIO module

# next, we need a command called 'sleep', so write

from time import sleep
# next we need to name all of the pins, so set the naming mode by writing

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
# this sets the names to board mode, which just names the pins according to the numbers in the middle of the diagram above.
# motor1 = Motor(16, 20, 12, my_pwm) #  DIG DIG PWM

# now we need to set the pins as outputs, so write

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
# now to setup the pwm commands type

pwm=GPIO.PWM(12, 100)
# next start the Pulse Width Modulation with 0 duty so it doesn't run yet

pwm.start(0)



GPIO.output(16, True)
GPIO.output(20, False)
# Now, we're going to set the PWM duty to 50%. Write

pwm.ChangeDutyCycle(50)
# then turn on the Enable pin

GPIO.output(12, True)
# then put the code to sleep for 2 seconds so the motor runs

sleep(7)
# now turn off the Enable pin

GPIO.output(12, False)
# then reverse the inputs to set it to reverse

GPIO.output(16, False)
GPIO.output(20, True)
# Then change the PWM duty to 75%

pwm.ChangeDutyCycle(75)
# then turn the enable back on

GPIO.output(12, True)
# put the code to sleep for 3 seconds

sleep(7)
# then turn the enable pin back off

GPIO.output(12, False)
# stop the Pulse

pwm.stop()
# and cleanup all of the GPIO channels.

GPIO.cleanup()
