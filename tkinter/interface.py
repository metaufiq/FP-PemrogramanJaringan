#import Tkinter
#top = Tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()


from tkinter import *
window = Tk()
window.title("capsa")


window.geometry('500x500')

btn = Button(window, text="login")
btn.grid(column=1, row=0)

window.mainloop()