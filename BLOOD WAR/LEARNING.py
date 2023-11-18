
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("600x500")


#top.configure(background = filename)
filename = PhotoImage(file = "Game")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#C.pack()
top.mainloop
