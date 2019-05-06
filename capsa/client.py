# Python program to implement client side of chat room. 
import socket 
import select 
import sys
import msvcrt
 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_address = "192.168.1.8" 
Port = 8080 
server.connect((IP_address, Port)) 
play = False

while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[],1)
    if msvcrt.kbhit(): read_sockets.append(sys.stdin) 
    


    for socks in read_sockets: 
        if socks == server:
            message = socks.recv(2048)
            command = message.split('_')
            print command
            if command[0] == 'NOTIFICATION':
                print command[1]+'\n\n'
            elif command[0] == 'CARDS':
                cardsOnHand = command[1].split(' ')

                print "Your cards are: "+ str(cardsOnHand) + '\n\n'

            elif command[0] == 'ONBOARD':
                cardsOnBoard = command[1].split(' ')
                print "cards on Board are: " + str(cardsOnBoard) +'\n\n'

            elif command[0] == 'PLAY':
                print "Your Turn\n\n"
                card = [1,2,3]
                message = sys.stdin.readline()
                message = card
                server.send(str(message)) 
                sys.stdout.write("<You>\n\n") 
                print message
                sys.stdout.flush()
server.close() 