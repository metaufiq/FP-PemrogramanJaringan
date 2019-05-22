import Tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#b7b7b7')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label = tk.Label(frame, text="Masukkan Email Anda", bg='#b7b7b7')
label.place(relx=0.37, rely=0.45)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0.37, rely=0.48,relwidth=0.26, relheight=0.05)


button = tk.Button(frame, text="Main", bg='black', fg='white', font=40)
button.place(relx=0.44, rely=0.56, relwidth=0.12, relheight=0.05)

root.mainloop()