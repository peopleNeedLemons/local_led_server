import optparse
import socket


def get_host_address():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.connect(("8.8.8.8", 80))
    host_address = server_socket.getsockname()[0]
    return server_socket, host_address


def get_port_param():
    option_parser = optparse.OptionParser()
    option_parser.add_option("-p", "--port")
    option_parser.add_option("-s", "--setup")
    (options, arguments) = option_parser.parse_args()
    if not options.port:
        option_parser.error("Please specify port by using -p argument")
    if options.setup:
        possible_setups = {"red", "green", "blue"}
        if options.setup not in possible_setups:
            option_parser.error("Possible options for -s command: " + str(possible_setups))

    return options
