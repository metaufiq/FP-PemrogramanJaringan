# Python program to implement client side of chat room. 
import socket 
import select 
import sys
import msvcrt
import pickle
from Message import *
 
  
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
            mail = socks.recv(2048)
            message = pickle.loads(mail)
            if message.type == 'NOTIFICATION':
                print message.message+'\n\n'

            elif message.type == 'PLAY':
                print "Your Turn\n\n"
                print"your cards: \n"
                i = 1
                for card in cardsOnHand:
                    print 'value:'+ str(card.value) + '\ttype:' + str(card.type) + '\n'
                    
                    i+=1
                
                card = 0
                card = input("\nselect card: ")
                card = card - 1

                server.send(pickle.dumps(cardsOnHand[card]))
                sys.stdout.write("\n\nselected card: \n") 
                print "value: " + str(cardsOnHand[card].value) + "\ttype: " + str(cardsOnHand[card].type) + "\n\n"
                cardsOnHand.remove(cardsOnHand[card])

                sys.stdout.flush()
            elif message.type == 'ONBOARD':
                cardsOnBoard = message.message

                print "cards on board: \n"
                for card in cardsOnBoard:
                    print 'value:'+ str(card.value) + '\ttype:' + str(card.type) + '\n'
                        
            elif message.type == 'PLAYER':
                player = message.message
                print "cards sending to you"
                cardsOnHand = player.getCards()
server.close() 