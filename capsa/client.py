# Python program to implement client side of chat room. 
import socket 
import select 
import sys
import msvcrt
import pickle
 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_address = "192.168.1.8" 
Port = 8080 
server.connect((IP_address, Port)) 
play = False
cardsOnHand = []
cardsOnBoard = []

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
            if command[0] == 'NOTIFICATION':
                print command[1]+'\n\n'

            elif command[0] == 'ONBOARD':
                cardsOnBoard = command[1].split(' ')
                print "cards on Board are: " + str(cardsOnBoard) +'\n\n'

            elif command[0] == 'PLAY':
                print "Your Turn\n\n"
                for card in cardsOnHand:
                    print 'card value:'+ str(card.value) + 'card type:' + str(card.type) + '\n\n'
                sys.stdout.write("\n\n<Command>: ") 
                message = sys.stdin.readline()
                server.send(str(message)) 
                sys.stdout.write("<You>\n\n") 
                print message
                sys.stdout.flush()
            else:
                player = pickle.loads(message)
                print "cards sending to you"
                cardsOnHand = player.getCards()
server.close() 