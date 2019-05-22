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


root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()  
