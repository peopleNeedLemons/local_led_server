import pigpio
from flask import request


def get_colour_field_from_request(field_name):
    try:
        return request.json[field_name]
    except KeyError:
        return 0


def change_rgb():
    red = get_colour_field_from_request("red")
    green = get_colour_field_from_request("green")
    blue = get_colour_field_from_request("blue")

    print(str(red))
    print(str(green))
    print(str(blue))

    pi = pigpio.pi()
    pi.set_PWM_dutycycle(17, red)  # red
    pi.set_PWM_dutycycle(22, green)  # green
    pi.set_PWM_dutycycle(24, blue)  # blue
    pi.stop()

    return "OK"
