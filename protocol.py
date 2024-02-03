#   Ex. 2.7 template - protocol
import socket
import pickle

LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """

    # (3)
    return True


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    pickled_data = pickle.dumps(data)

    length = str(len(pickled_data)).zfill(4)
    payload = length.encode() + pickled_data
    return payload
# (4)

def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length = my_socket.recv(10).decode()
    if(length.isdigit()):
        msg = my_socket.recv(int(length)).decode()
        return msg
    return False,"Error"
 # (5)

