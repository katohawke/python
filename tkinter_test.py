#!/usr/bin/env python3

from tkinter import *

def button_clicked():
	print("Hello World!")

mw = Tk()
mw.title('Hello World!')
mw.geometry('300x40')

button = Button(mw, text="Press Me", command=button_clicked)
button.pack(fill=BOTH)

mw.mainloop()