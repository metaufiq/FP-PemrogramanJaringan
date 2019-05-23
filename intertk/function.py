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


def chat(root):
    window = tk.Toplevel(root)
    window.resizable(width=False, height=False)

    HEIGHT = 300
    WIDTH = 800

    window.title('Chat Capsa')

    canvaschat = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    canvaschat.pack()

    framechat = tk.Frame(window, bg='#fff3e1')
    framechat.place(relx=0, rely=0, relwidth=1, relheight=1)

    entrychat = tk.Entry(framechat, bg='white', bd=0, justify='left')
    entrychat.place(relx=0.05, rely=0.8,relwidth=0.7, relheight=0.12)

    button = tk.Button(framechat, text="Kirim", bg='black', fg='white', bd=0, activebackground='#fff3e1', command=lambda: printchat(entrychat.get()))
    button.place(relx=0.75, rely=0.8, relwidth=0.2, relheight=0.12)

def printchat(entrychat):
	print entrychat