import time
from flask import *
# import pigpio
import RPi.GPIO as GPIO # import GPIO librery
# import p1.pwm

# define pins
SERVO_X_PIN  = 28
SERVO_Y_PIN  = 29

# define servo range
SERVO_X_MIN = 730
SERVO_X_MAX = 3200
SERVO_X_START = 1950

SERVO_Y_MIN = 770
SERVO_Y_MAX = 2000
SERVO_Y_START = 1450

# initialize servo
time.sleep(1)
# p1.pwm.servo(SERVO_X_PIN, SERVO_X_START)
# p1.pwm.servo(SERVO_Y_PIN, SERVO_Y_START)

# Create flask app and global pi 'thing' object.
app = Flask(__name__)

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    # return render_template('index.html')
    return ('Unknown control', 400)

# LED route allows changing the LED state with a POST request.
# @app.route("/control/<path:state>", methods=['POST'])
@app.route("/control/<path:state>")
def control(state):
    # Set direction
    if state == 'direction/forward':
        print('forward')
        # p1.pwm.duty(0, 100, 10000)
        # p1.pwm.duty(1, 50, 0)
        # motorLeft.forward(50)
        # motorRight.forward(50)
    elif state == 'direction/backward':
        print('backward')
        # p1.pwm.duty(0, 50, 20000)
        # p1.pwm.duty(1, 50, 0)
        # motorLeft.backward(50)
        # motorRight.backward(50)
    elif state == 'direction/left':
        print('left')
        # p1.pwm.servo(SERVO_Y_PIN, SERVO_Y_MIN)
    elif state == 'direction/right':
        print('right')
        # p1.pwm.servo(SERVO_Y_PIN, SERVO_Y_MAX)
    elif state == 'direction/stop':
        print('stop')
        # p1.pwm.duty(0, 50, 0)
        # p1.pwm.duty(1, 50, 0)
        # motorLeft.stop()
        # motorRight.stop()
        return ('stop', 200)
    elif state == 'direction/combined':
        # print "combined"
        directionY = int(float(request.form['directionY']))
        directionX = int(float(request.form['directionX']))
        # print "dirY: ", directionY
        # print "dirX: ", directionX
        # keeping variable in range 0-100
        if directionY > 100:
            directionY = 100
        if directionY < -100:
            directionY = -100
        if directionX > 100:
            directionX = 100
        if directionX < -100:
            directionX = -100

        # basic direction
        # if directionY >= 0:
        #     # # print directionY
        #     motorLeft.forward(directionY)
        # elif directionY <= 0:
        #     # # print directionY
        #     motorLeft.forward(-directionY)
        #
        # if directionX >= 0:
        #     motorRight.forward(directionX)
        # elif directionX <= 0:
        #     motorRight.forward(-directionX)
        if directionY <= 0:
            print('some direction')
            # p1.pwm.duty(0, -directionY, 100)
            # p1.pwm.duty(1, 50, 0)
            # motorLeft.forward(-directionY)
            # motorRight.forward(-directionY)



    else:
        return ('Unknown control', 400)
    return ('', 204)

# Server-sent event endpoint that streams the thing state every second.
@app.route('/thing')
def thing():
    def get_thing_values():
        while True:
            # Build up a dict of the current thing state.
            thing_state = {
                'switch': pi_thing.read_switch(),
                # 'temperature': pi_thing.get_temperature(),
                # 'humidity': pi_thing.get_humidity()
            }
            # Send the thing state as a JSON object.
            yield('data: {0}\n\n'.format(json.dumps(thing_state)))
            # Wait a second and repeat.
            time.sleep(1.0)
    return Response(get_thing_values(), mimetype='text/event-stream')

# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
#
    app.run(host='0.0.0.0', port=8099, debug=True, threaded=True)
    # app.run(host='0.0.0.0', port=8089, debug=False, threaded=True)
