#!/usr/bin/env/python
# coding=utf-8


from tkinter import *
import pickle


class PhoneList:

    phonelist = {}
    temporarylist = {}
    phonelistfile = 'phonelist.data'

    def __init__(self, name, phone):

        self.name = name
        self.phone = phone
        PhoneList.phonelist[name] = phone

    @staticmethod
    def open(namelist):

        with open(PhoneList.phonelistfile, 'rb') as f:
            namelist.update(pickle.load(f))

    @staticmethod
    def save(namelist):

        with open(PhoneList.phonelistfile, 'wb') as f:
            pickle.dump(namelist, f)

    @staticmethod
    def add():

        PhoneList.save(PhoneList.phonelist)
        PhoneList.open(PhoneList.temporarylist)
        PhoneList.save(PhoneList.temporarylist)

    @staticmethod
    def show(main):
        try:
            PhoneList.open(PhoneList.temporarylist)
            if len(PhoneList.temporarylist) != 0:
                List(main, name='Name', phone='Phone')
                for person in PhoneList.temporarylist:
                    List(main, name=person, phone=PhoneList.temporarylist[person])
        except EOFError:
            pass


class File:

    def __init__(self, main):

        self.file = Menu(main)
        main.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='New')


class Edit:

    def __init__(self, main):

        self.edit = Menu(main)
        main.add_cascade(label='Edit', menu=self.edit)
        self.edit.add_command(label='Add')
        self.edit.add_command(label='Change')
        self.edit.add_command(label='Find')
        self.edit.add_command(label='Delete')


class List:

    row = 0

    def __init__(self, main, name, phone):

        self.label_list_name = Label(main, text=name)
        self.label_list_phone = Label(main, text=phone)
        self.label_list_name.grid(row=List.row, column=0)
        self.label_list_phone.grid(row=List.row, column=1)
        List.row += 1


class View:

    global frame_list

    def __init__(self, main):

        self.view = Menu(main)
        main.add_cascade(label='View', menu=self.view)
        self.view.add_command(label='Show', command=View.__show(main))

    @staticmethod
    def __show(main):
        PhoneList.show(main)


root = Tk()

menu = Menu(root)
root.configure(menu=menu)

file = File(menu)
edit = Edit(menu)
show = View(menu)

frame_list = Frame(root)
frame_list.pack()

List(frame_list, 'Name', 'Phone')

root.mainloop()
