#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020
import socket
import protocol
import os
import commands

IP = '0.0.0.0'
PORT = 1729
#PHOTO_PATH = ???? # The path + filename where the screenshot at the server should be saved
ALL = {
        "screenshot": 0,
        "dir": 1,
        "delete": 1,
        "copy": 2,
        "execute": 1,
        "exit": 0,
        "send_screenshot": 0
}

def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: List of the cmd params (ex. ["c:\\cyber"])
    """
    # Use protocol.check_cmd first

    # Then make sure the params are valid

    # (6)
    broken = cmd.split(' ')
    print(broken)
    print(broken[0])
    if(broken[0]=='screenshot'):
        return True,broken[0]
    if(broken[0]=='delete' or 'execute' ):
        print((os.path.isfile(broken[1])))
        if((os.path.isfile(broken[1]))):
            return True, broken[0],broken[1]
    if(broken[0]=='dir'):
        if(os.path.exists(broken[1])):
            print(broken)
            return True, broken[0], broken[1]
    if(broken[0]=='copy'):
        copy_split = broken[1].split(',')
        print((os.path.isfile(copy_split[0])==True) and (os.path.exists(copy_split[1])==True))
        if((os.path.isfile(copy_split[0])==True) and (os.path.exists(copy_split[1])==True)):
            return True, broken[0],copy_split
    print("false")
    return False, broken[0],broken[1]

def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """
    if (command == 'delete'):
        response = commands.delete(params)
    if (command == 'dir'):
        print("inside2")
        response = commands.dir(params)
        print(response)
    if (command == 'copy'):
        response = commands.copy(params[0],params[1])
    if (command == 'execute'):
        response = commands.execute(params)
    if (command == 'screenshot'):
        response = commands.screenshot()
    if (command == 'send_screenshot'):
        response = commands.send_screenshot()
    if (command == 'exit'):
        response = commands.exit()
    # (7)
    return response


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    # (1)

    # handle requests until user asks to exit
    while True:
        # Check if protocol is OK, e.g. length field OK
        valid_protocol, cmd = protocol.get_msg(client_socket)
        if valid_protocol:
            # Check if params are good, e.g. correct number of params, file name exists
            print(cmd)
            if(cmd== 'screenshot'):
                msg = handle_client_request(cmd,' ')
                ready_msg = protocol.create_msg(msg)
                client_socket.send(ready_msg.encode())
            elif(cmd == 'send_screenshot'):
                msg = handle_client_request(cmd, ' ')
                ready_msg = protocol.create_msg(msg)
                client_socket.send(ready_msg.encode())
            else:
                valid_cmd, command, params = check_client_request(cmd)
                if valid_cmd:

                    # (6)
                    msgold = handle_client_request(command,params)
                    # prepare a response using "handle_client_request"

                    if(command == 'dir'):
                        msg2 = '" "'.join(msgold)
                        msg = msg2
                        print("msg:  " + msg  )
                        ready_msg = protocol.create_msg(msg)
                    elif(command == 'delete' or 'execute' or 'screenshot'):
                        ready_msg = protocol.create_msg(msgold)
                    # add length field using "create_msg"
                    client_socket.send(ready_msg.encode())
                    # send to client
                        # Send the data itself to the client

                        # (9)

                    if command == 'exit':
                        print("Closing connection")
                        client_socket.close()
                        server_socket.close()
                else:
                    # prepare proper error to client
                    response = 'Bad command or parameters'
                    # send to client
                    client_socket.send(response.encode())
        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            #send to client
            client_socket.send(response.encode())
            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")
    client_socket.close()
    server_socket.close()

main()
