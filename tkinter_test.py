#!/usr/bin/env/python
# coding=utf-8

from tkinter import *
import time


def button_clicked():
    button['text'] = time.strftime('%H:%M:%S')


root = Tk()

button = Button(root)
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)

button.pack()

root.mainloop()
