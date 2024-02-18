#   Ex. 2.7 template - protocol

import pickle

LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    ALL = {
        "screenshot": 0,
        "dir": 1,
        "delete": 1,
        "copy": 1,
        "execute": 1,
        "exit": 0,
        "send_screenshot": 0
    }
    Command = data.split(' ')
    if (Command[0] in ALL.keys() and len(Command) == 1 + ALL[Command[0]]):
        return True
    return False

def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    length = str(len(data))
    amount = 10-len(length)
    num = ''
    while(amount > 0):
        num +='0'
        amount-=1
    num+=length
    return num + data
# (4)

def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    print("Got msg")
    length = my_socket.recv(10).decode()
    if(length.isdigit()):
        msg = my_socket.recv(int(length)).decode()
        return True,msg
    return False,"Error"
 # (5)

