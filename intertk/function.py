import Tkinter as tk
from PIL import Image, ImageTk
import tkMessageBox

def play(root):
   	frameGame = tk.Frame(root, bg='#000000')
   	frameGame.place(relx=0, rely=0, relwidth=1, relheight=1)
   	load = Image.open("../asset/meja.png")
	render = ImageTk.PhotoImage(load)
	img = tk.Label(frameGame, image=render, bg='#fff3e1')
	img.image = render
	img.place(relx=0, rely=0, relwidth=1, relheight=1)

	frameLeft = tk.Frame(frameGame, bg='#f4f142')
	frameLeft.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.6)

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