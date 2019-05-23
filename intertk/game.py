import Tkinter as tk
from PIL import ImageTk,Image

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.resizable(width=False, height=False)
root.title('Capsa')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


 
background_image = ImageTk.PhotoImage(Image.open("../asset/meja.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0 ,relwidth=1, relheight=1)



frameLeft = tk.Frame(background_label, bg='#f4f142')
frameLeft.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.6)

yPosition = 0
backcards = ImageTk.PhotoImage(Image.open("../asset/asset kartu/Deck2.gif").resize((135,120), Image.ANTIALIAS))
cardsLeft= []

for i in range(13):
    cardsLeft.append(tk.Label(frameLeft, image=backcards))
    cardsLeft[i].place(relx=0, rely=yPosition , relwidth=1, relheight=0.3)
    yPosition+=0.07


frameRight = tk.Frame(background_label, bg='#f46242')
frameRight.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)

yPosition = 0
cardsRight= []
for i in range(13):
    cardsRight.append(tk.Label(frameRight, image=backcards))
    cardsRight[i].place(relx=0, rely=yPosition, relwidth=1, relheight=0.3)
    yPosition+=0.07

frameTop= tk.Frame(background_label, bg='#42f453')
frameTop.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=0.1)

xPosition = 0
cardsTop= []
for i in range(13):
    cardsTop.append(tk.Label(frameTop, image=backcards))
    cardsTop[i].place(relx=xPosition, rely=0, relwidth=0.3, relheight=1)
    xPosition+=0.07

frameBottom = tk.Frame(background_label, bg='#4268f4')
frameBottom.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)


root.mainloop()
