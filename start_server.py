from flask import Flask

from colours import change_rgb
from local_utils import get_host_address

app = Flask(__name__)


@app.route('/hello_there')
def buenos_dias():
    return "buenos dias"


@app.route('/colour', methods=['PUT'])
def set_colour():
    return change_rgb()


if __name__ == '__main__':
    server_socket, host_address = get_host_address()

    app.run()
    server_socket.close()
