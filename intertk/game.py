import Tkinter as tk
from PIL import ImageTk,Image

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


 
background_image = ImageTk.PhotoImage(Image.open("../asset/meja.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0 ,relwidth=1, relheight=1)



frameLeft = tk.Frame(background_label, bg='#f4f142')
frameLeft.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.6)




frameRight = tk.Frame(background_label, bg='#f46242')
frameRight.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)

frameUp= tk.Frame(background_label, bg='#42f453')
frameUp.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=0.1)

background_clubs3 = ImageTk.PhotoImage(Image.open("../asset/asset kartu/Deck2.gif").resize((12,120), Image.ANTIALIAS))
background_card3 = tk.Label(frameLeft, image=background_clubs3)
background_card3.place(x=0, rely=0.1 ,relwidth=1, relheight=0.3)

frameBottom = tk.Frame(background_label, bg='#4268f4')
frameBottom.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)


root.mainloop()
