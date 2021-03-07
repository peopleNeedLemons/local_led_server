import pigpio
from flask import request, jsonify

from models.ColourToChange import ColourToChange
from statuses import success_status_code, server_error_code


# todo: add some proxy layer

def get_colour_field_from_request(field_name):
    try:
        return request.json[field_name]
    except KeyError:
        return 0


def ping_pig_to_change_colour(new_colour):
    pi = pigpio.pi()
    result_red = pi.set_PWM_dutycycle(17, new_colour.red)
    result_green = pi.set_PWM_dutycycle(22, new_colour.green)
    result_blue = pi.set_PWM_dutycycle(24, new_colour.blue)
    pi.stop()

    return result_red > 0 and result_green > 0 and result_blue > 0


def change_rgb():
    red = get_colour_field_from_request("red")
    green = get_colour_field_from_request("green")
    blue = get_colour_field_from_request("blue")

    print(str(red))
    print(str(green))
    print(str(blue))

    change_colour_request = ColourToChange(red, green, blue)
    change_colour_result = ping_pig_to_change_colour(change_colour_request)

    if change_colour_result:
        json_response = jsonify(status=success_status_code, red=red, green=green, blue=blue)
    else:
        json_response = jsonify(status=server_error_code, message="Colour changing problem")
    return json_response


def prepare_rgb_pre_set(pre_set):
    setup_colour_to_change = {
        "red": ColourToChange(255, 0, 0),
        "green": ColourToChange(0, 255, 0),
        "blue": ColourToChange(0, 0, 255)
    }.get(pre_set, ColourToChange(0, 0, 0))

    ping_pig_to_change_colour(setup_colour_to_change)
