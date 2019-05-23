import Tkinter as tk
from PIL import ImageTk,Image

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='table.jpg')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
    
frame = tk.Frame(root, bg='pink')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0.37, rely=0.48,relwidth=0.26, relheight=0.05)


button = tk.Button(frame, text="Main", bg='black', fg='white', font=40)
button.place(relx=0.44, rely=0.56, relwidth=0.12, relheight=0.05)

root.mainloop()
