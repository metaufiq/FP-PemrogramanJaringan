import Tkinter as tk
import request
from PIL import ImageTk,Image

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("C:\Users\ASUS\Documents\GitHub\FP-PemrogramanJaringan\intertk\meja.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0 ,relwidth=1, relheight=1)


root.mainloop()
