import Tkinter as tk
from PIL import Image, ImageTk
import tkMessageBox

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.resizable(width=False, height=False)

root.title('Capsa')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#fff3e1')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

load = Image.open("../asset/asset logo/instagram_profile_image.png").resize((400, 400), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = tk.Label(frame, image=render, bg='#fff3e1')
img.place(relx=0.35, rely=0.16, relwidth=0.3, relheight=0.3)

label = tk.Label(frame, text="Masukkan Email Anda", bg='#fff3e1')
label.place(relx=0.37, rely=0.55, relwidth=0.26)

entry = tk.Entry(frame, bg='white', bd=0, font=40, justify='center')
entry.place(relx=0.37, rely=0.6,relwidth=0.26, relheight=0.05)

def mulai(entry):
	print(entry)
   	framegame = tk.Frame(root, bg='#000000')
   	framegame.place(relx=0, rely=0, relwidth=1, relheight=1)
   	load = Image.open("../asset/meja.png")
	render = ImageTk.PhotoImage(load)
	img = tk.Label(framegame, image=render, bg='#fff3e1')
	img.image = render
	img.place(relx=0, rely=0, relwidth=1, relheight=1)

	frameLeft = tk.Frame(framegame, bg='#f4f142')
	frameLeft.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.6)

	yPosition = 0
	load = Image.open("../asset/asset kartu/Deck2.gif")
	render = ImageTk.PhotoImage(load)
	
	yPosition = 0
	cardsRight= []
	for i in range(13):
		card = tk.Label(frameLeft, image=render, bg='#fff3e1')
		card.image = render
		cardsRight.append(card)
		cardsRight[i].place(relx=0, rely=yPosition, relwidth=1, relheight=0.3)
		yPosition+=0.07

button = tk.Button(frame, text="Mulai", bg='black', fg='white', font=40, bd=0, activebackground='#fff3e1', command=lambda: mulai(entry.get()))
button.place(relx=0.44, rely=0.67, relwidth=0.12, relheight=0.05)

def tentang():
   tkMessageBox.showinfo( "Tentang", "Capsa oleh Kelompok 2 Pemrograman Jaringan kelas C")

button = tk.Button(frame, text="Tentang", bg='#fff3e1', fg='black', bd=0, activebackground='#fff3e1', command= tentang)
button.place(relx=0.44, rely=0.9, relwidth=0.12, relheight=0.05)



root.mainloop()