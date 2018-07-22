import time
from flask import *

from motor import Motor

my_pwm = 100
motor1 = Motor(16, 20, 12, my_pwm) #  DIG DIG PWM
motor2 = Motor(5, 6, 13, my_pwm) #  DIG DIG PWM

# motor2 = Motor(5, 6, 16, my_pwm)
#
# Create flask app and global pi 'thing' object.
app = Flask(__name__)

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    # return render_template('index.html')
    return ('Unknown controls', 400)

# LED route allows changing the LED state with a POST request.
@app.route("/controls/<path:state>", methods=['POST'])
# @app.route("/controls/<path:state>")
def control(state):
    # Set direction
    if state == 'direction/glove':
        # print('glove')
        # print(request.json)
        received = request.form['sensor1']
        print("Received : "+ received)

        percentage = int(received) * ( 100 / 255 )
        print("Percentage: " + str(percentage))
        # Considering the flex sensor (http://adafru.it/1070) a reading range is between 40% and 92%
        return "200"
        # p1.pwm.duty(0, 100, 10000)
        # p1.pwm.duty(1, 50, 0)
        # motorLeft.forward(50)
        # motorRight.forward(50)
    if state == 'direction/forward':

        motor1.forward(abs(100))
        motor2.forward(abs(100))

    elif state == 'direction/backward':

        motor1.backward(abs(100))
        motor2.backward(abs(100))

    elif state == 'direction/left':

        motor1.backward(abs(100))
        motor2.forward(abs(100))

    elif state == 'direction/right':

        motor1.forward(abs(100))
        motor2.backward(abs(100))

    elif state == 'direction/stop':

        print('stop')
        motor1.stop()
        motor2.stop()

        return ('stop', 200)

    elif state == 'direction/combined':

        directionY = int(float(request.form['directionY']))
        directionX = int(float(request.form['directionX']))

        # Preventing that the variable excesses 100 or -100
        if directionY > 100:
            directionY = 100
        if directionY < -100:
            directionY = -100

        if directionX > 100:
            directionX = 100
        if directionX < -100:
            directionX = -100

        # basic direction
        if directionY >= 0:

            print('backward')
            motor1.backward(abs(directionY))
            motor2.backward(abs(directionY))

        elif directionY <= 0:

            print('forward')
            motor1.forward(abs(directionY))
            motor2.forward(abs(directionY))

        return('OK',200)

    else:
        return ('Unknown control', 400)
    return ('', 204)

# Server-sent event endpoint that streams the thing state every second.
@app.route('/thing')
def thing():
    def get_thing_values():
        while True:
            # Build up a dict of the current thing state.
            # thing_state = {
            #     'switch': pi_thing.read_switch(),
            #     'temperature': pi_thing.get_temperature(),
            #     'humidity': pi_thing.get_humidity()
            # }
            # Send the thing state as a JSON object.
            yield('data: {0}\n\n'.format(json.dumps(thing_state)))
            # Wait a second and repeat.
            time.sleep(1.0)
    return Response(get_thing_values(), mimetype='text/event-stream')

# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":

    # app.run(host='0.0.0.0', port=8099, debug=True, threaded=True, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
    # app.run(host='0.0.0.0', port=8089, debug=True, threaded=True)
    app.run(host='0.0.0.0', port=8089, debug=False, threaded=True)
