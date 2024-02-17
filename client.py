#   Ex. 2.7 template - client side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import socket
import protocol


IP = '127.0.0.1'
PORT = 1729
#SAVED_PHOTO_LOCATION = ???? # The path + filename where the copy of the screenshot at the client should be saved

def handle_server_response(my_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request
    For example, DIR should result in printing the contents to the screen,
    Note- special attention should be given to SEND_PHOTO as it requires and extra receive
    """
    save = cmd.split(' ')
    if(save[0] == 'dir'):
        fixed = protocol.get_msg(my_socket)
        list = fixed[1].split('ывффцй')
        print(list)
     # (8) treat all responses except SEND_PHOTO
    elif(save[0]!='send_screenshot' or 'dir'):
        fixed = protocol.get_msg(my_socket)
        print(fixed[1])
    # (10) treat SEND_PHOTO
    #else

def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    # (2)

    # print instructions
    print('Welcome to remote computer application. Available commands are:')
    print('screenshot\nsend_screenshot\ndir\ndelete\ncopy\nexecute\nexit')

    # loop until user requested to exit
    cmd =""
    while True:
        cmd = input("Please enter command:\n")
        if protocol.check_cmd(cmd):
            packet = protocol.create_msg(cmd)
            my_socket.send(packet.encode())
            handle_server_response(my_socket, cmd)
            if cmd == 'EXIT':
                break
        else:
            print("IN CLIENT")
            print("Not a valid command, or missing parameters\n")

    my_socket.close()

main()