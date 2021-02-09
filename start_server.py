from flask import Flask
from flask import request
import pigpio
import socket

app = Flask(__name__)


@app.route('/hello_there')
def buenos_dias():
    return "buenos dias"

@app.route('/colour', methods=['PUT'])
def set_colour():

    blue = request.json["blue"]
    red = request.json["red"]
    green = request.json["green"]

    if blue is None:
        blue = 0

    if red is None:
        red = 0

    if green is None:
        green = 0

    pi = pigpio.pi()
    pi.set_PWM_dutycycle(17, red) #red
    pi.set_PWM_dutycycle(22, green) #green
    pi.set_PWM_dutycycle(24, blue) #blue
    pi.stop()

    return "OK"

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.connect(("8.8.8.8", 80))
    host_address = server_socket.getsockname()[0]

    app.run(host=host_address, port=5001)
    server_socket.close()