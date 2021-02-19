import socket


def get_host_address():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.connect(("8.8.8.8", 80))
    host_address = server_socket.getsockname()[0]
    return server_socket, host_address
