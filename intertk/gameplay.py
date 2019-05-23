import Tkinter as tk
from PIL import Image, ImageTk
import tkMessageBox
from Message import *
from Player import *
from thread import *
import pickle
import socket
import select 
import sys
import msvcrt

class GamePlay():
	cardsOnHand = []
	cardsOnBoard = []
	player = 0

	def chat(self,root):
		window = tk.Toplevel(root)
		window.resizable(width=False, height=False)

		HEIGHT = 300
		WIDTH = 800

		window.title('Chat Capsa')

		canvaschat = tk.Canvas(window, height=HEIGHT, width=WIDTH)
		canvaschat.pack()

		self.framechat = tk.Frame(window, bg='#fff3e1')
		self.framechat.place(relx=0, rely=0, relwidth=1, relheight=1)

		entrychat = tk.Entry(self.framechat, bg='white', bd=0, justify='left')
		entrychat.place(relx=0.05, rely=0.8,relwidth=0.7, relheight=0.12)

		button = tk.Button(self.framechat, text="Kirim", bg='black', fg='white', bd=0, activebackground='#fff3e1', command=lambda: self.printchat(entrychat.get()))
		button.place(relx=0.75, rely=0.8, relwidth=0.2, relheight=0.12)

	def printchat(self,entrychat):
		print entrychat
		labelchat = tk.Label(self.framechat, text=entrychat, bg='#fff3e1', font=50)
		labelchat.place(relx=0.37, rely=0.55, relwidth=0.26)

	def playGame(self,root):
		frameGame = tk.Frame(root, bg='#000000')
		frameGame.place(relx=0, rely=0, relwidth=1, relheight=1)
		load = Image.open("../asset/meja.png")
		render = ImageTk.PhotoImage(load)
		img = tk.Label(frameGame, image=render, bg='#fff3e1')
		img.image = render
		img.place(relx=0, rely=0, relwidth=1, relheight=1)

		frameLeft = tk.Frame(frameGame, bg='#f4f142')
		frameLeft.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.6)
		
		load = Image.open("../asset/asset kartu/number_2_type_3.png").resize((175,212), Image.ANTIALIAS)
		render = ImageTk.PhotoImage(load)
		card = tk.Label(frameGame, image=render, bg='#fff3e1')
		card.image = render
		card.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.3)	
		load = Image.open("../asset/asset kartu/Deck2.gif")
		render = ImageTk.PhotoImage(load)
		
		yPosition = 0
		cardsLeft= []
		for i in range(13):
			card = tk.Label(frameLeft, image=render, bg='#fff3e1')
			card.image = render
			cardsLeft.append(card)
			cardsLeft[i].place(relx=0, rely=yPosition, relwidth=1, relheight=0.3)
			yPosition+=0.07
		
		frameRight = tk.Frame(frameGame, bg='#f46242')
		frameRight.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)

		yPosition = 0
		cardsRight= []
		for i in range(13):
			card = tk.Label(frameRight, image=render, bg='#fff3e1')
			card.image = render
			cardsRight.append(card)
			cardsRight[i].place(relx=0, rely=yPosition, relwidth=1, relheight=0.3)
			yPosition+=0.07
		
		frameTop= tk.Frame(frameGame, bg='#42f453')
		frameTop.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=0.1)

		xPosition = 0
		cardsTop= []
		for i in range(13):
			card = tk.Label(frameTop, image=render, bg='#fff3e1')
			card.image = render
			cardsTop.append(card)
			cardsTop[i].place(relx=xPosition, rely=0, relwidth=0.18, relheight=1)
			xPosition+=0.07

		self.frameBottom = tk.Frame(frameGame, bg='#4268f4')
		self.frameBottom.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		IP_address = "192.168.1.8" 
		Port = 8080 
		self.server.connect((IP_address, Port)) 
		start_new_thread(self.clientThread,())   

		
	def clientThread(self):
		while True:
			# maintains a list of possible input streams 
			sockets_list = [self.server] 
		
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
				if socks == self.server:
					mail = socks.recv(2048)
					message = pickle.loads(mail)
					if message.type == 'NOTIFICATION':
						#print message.message+'\n\n'
						pass
					elif message.type == 'PLAY':
						print "Your Turn\n\n"
						print"your cards: \n"

						for card in self.cardsOnHand:
							print 'value:'+ str(card.number) + '\ttype:' + str(card.type) + '\n'
							
						
						card = 0
						card = input("\nselect card: ")
						card = card - 1

						if self.cardsOnBoard:
							while self.cardsOnBoard[0].value > self.cardsOnHand[card].value:
								print("your cards have lower value than card on board...\n\n")
								card = input("select card...again: ")
						

						self.server.send(pickle.dumps(self.cardsOnHand[card]))
						sys.stdout.write("\n\nselected card: \n") 
						print "value: " + str(self.cardsOnHand[card].value) + "\ttype: " + str(self.cardsOnHand[card].type) + "\n\n"
						self.cardsOnHand.remove(self.cardsOnHand[card])

						sys.stdout.flush()
					elif message.type == 'ONBOARD':
						self.cardsOnBoard = message.message

						print "cards on board: \n"
						for card in self.cardsOnBoard:
							print 'value:'+ str(card.number) + '\ttype:' + str(card.type) + '\n'

					elif message.type == 'PLAYER':
						self.player = message.message
						print "cards sending to you"
						self.cardsOnHand = self.player.getCards()
						
						xPosition = 0
						cardsBottom = []
						for card in self.cardsOnHand:
							print 'number:'+ str(card.number) + '\ttype:' + str(card.type) + '\n'
							load = Image.open("../asset/asset kartu/number_"+str(card.number)+"_type_"+str(card.type)+".png").resize((80,70), Image.ANTIALIAS)
							render = ImageTk.PhotoImage(load)
							cardModel = tk.Button(self.frameBottom, image=render, bg='#fff3e1')
							cardModel.image = render
							cardsBottom.append(cardModel)
							cardsBottom[-1].place(relx=xPosition, rely=0, relwidth=0.18, relheight=1)
							
							xPosition+=0.07

		self.server.close() 