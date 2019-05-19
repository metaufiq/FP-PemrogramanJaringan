import Tkinter
from Tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Capsa")

        self.label = Label(master, text="Welcome To Capsa")
        self.label.pack()

        self.greet_button = Button(master, text="Login", command=self.login)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.client_exit)
        self.close_button.pack()

    def login(self):
        print("Greetings!")

    def client_exit(self):
        exit()

root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("400x300")
root.mainloop()
