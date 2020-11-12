from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")


def popup():
    response = messagebox.askokcancel("warning", "Hello Sudheer")
    if response == 1:
        Label(root, text="you said Okay!").pack()
    else:
        Label(root, text="you said NO!").pack()


button1 = Button(root, text="Pressit!", command=popup).pack()

root.mainloop()
