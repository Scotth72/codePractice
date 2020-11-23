from tkinter import *

root = Tk()

e= Entry(root, width="50", borderwidth="5")
e.pack()
e.insert(0, "Enter Your Name: ")

def myCick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", fg="blue", command=myCick)
myButton.pack()

root.mainloop()
