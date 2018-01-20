import p1.pwm
import time

# p1.pwm.servo(28, 800)
# p1.pwm.servo(29, 1200)
# time.sleep(10)

x = 400
while x < 3300:
    print x
    p1.pwm.servo(28, x)
    time.sleep(0.09)
    x=x+20


i = 600
while i < 2000:
    print i
    p1.pwm.servo(29, i)
    time.sleep(0.1)
    i=i+20
    # p1.pwm.servo(5, 500)
    # print 1
    # time.sleep(2)
    # p1.pwm.servo(5, 200)
    # print 2
    # time.sleep(2)
    # print 3
    # p1.pwm.servo(5, 65535)
