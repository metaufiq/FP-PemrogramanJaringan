import Tkinter
from Tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)             
        self.master = master
        self.init_window()

    def init_window(self):     
        self.master.title("Capsa")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        view = Menu(menu)
        view.add_command(label="Chat", command=self.new_window)
        menu.add_cascade(label="View", menu=view)
        account = Menu(menu)
        account.add_command(label="Login", command=self.new_window)
        menu.add_cascade(label="Account", menu=account)
        self.frame = Frame(self.master)
        self.b2 = Button(self.master, text="Login", command=self.new_window)
        self.b2.pack()
        self.frame.pack()

        load = Image.open("images (1).jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        load = Image.open("images (1).jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=200, y=13)

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Play(self.newWindow)


    def client_exit(self):
        exit()

class Play(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)             
        self.master = master
        self.master.geometry("800x600")
        self.init_window()

    def init_window(self):
        self.master.title("Capsa")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        account = Menu(menu)
        account.add_command(label="Login", command=self.new_window)
        menu.add_cascade(label="Account", menu=account)
        self.frame = Frame(self.master)
        self.b2 = Button(self.master, text="Login", command=self.new_window)
        self.b2.pack()
        self.frame.pack()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Play(self.newWindow)


    def client_exit(self):
        exit()


class email(frame):
    def test_function(entry):
    	print("input email:", entry)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="play", font=40, command=lambda: play(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()  
