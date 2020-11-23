from tkinter import *

root = Tk()

def myCick():
    myLabel = Label(root, text="Look, I clicked a Button!!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", fg="blue", command=myCick)
myButton.pack()

root.mainloop()