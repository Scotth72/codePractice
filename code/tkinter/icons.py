from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to use Icons")
root.iconbitmap('../icons/mando.png')

btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_quit.pack()

root.mainloop()