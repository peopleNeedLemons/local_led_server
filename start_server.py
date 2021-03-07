from flask import Flask

from colour_changer import change_rgb, prepare_rgb_pre_set
from local_utils import get_host_address, get_port_param

app = Flask(__name__)


@app.route('/hello_there')
def buenos_dias():
    return "buenos dias"


@app.route('/colour', methods=['PUT'])
def set_colour():
    return change_rgb()


if __name__ == '__main__':
    server_socket, host_address = get_host_address()
    params = get_port_param()

    if params.setup:
        prepare_rgb_pre_set(params.setup)

    app.run(host=host_address, port=params.port)

    server_socket.close()
