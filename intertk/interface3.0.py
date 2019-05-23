import Tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#fff3e1')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

load = Image.open("./asset logo/instagram_profile_image.png").resize((300, 300), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = tk.Label(frame, image=render, bg='#fff3e1')
img.image = render
img.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.3)

label = tk.Label(frame, text="Masukkan Email Anda", bg='#fff3e1')
label.place(relx=0.37, rely=0.55)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0.37, rely=0.6,relwidth=0.26, relheight=0.05)


button = tk.Button(frame, text="Mulai", bg='black', fg='white', font=40)
button.place(relx=0.44, rely=0.67, relwidth=0.12, relheight=0.05)

root.mainloop()