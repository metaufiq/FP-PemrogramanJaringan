import Tkinter
from Tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)             
        self.master = master
        self.init_window()

    def init_window(self):     
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        account = Menu(menu)
        account.add_command(label="Login", command=self.client_exit)
        menu.add_cascade(label="Account", menu=account)
        self.frame = Frame(self.master)
        self.b2 = Button(self.master, text="Button2", command=self.new_window)
        self.b2.pack()
        self.frame.pack()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Buttons1(self.newWindow)

    def client_exit(self):
        exit()

class Buttons1():
    
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.b3 = Button(self.master, text="Button3", command=self.display3)
        self.b3.pack()
        self.frame.pack()

    def display3(self):
        print 'hello button3'


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()  
