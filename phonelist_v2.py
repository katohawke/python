#!/usr/bin/env/python
# coding=utf-8


from tkinter import *
from tkinter import messagebox
import pickle


class List:

    row = 0

    def __init__(self, main, name, phone):

        self.main = main
        self.name = name
        self.phone = phone
        self.label_list_name = Label(main, text=name)
        self.label_list_phone = Label(main, text=phone)
        self.label_list_name.grid(row=List.row, column=0)
        self.label_list_phone.grid(row=List.row, column=1)
        List.row += 1

    def remove(self):
        self.label_list_phone.grid_forget()
        self.label_list_name.grid_forget()


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



class MainMenu(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.parent = parent
        self.viewable_objects = []
        self.message = StringVar()
        self.initUI()

    def initUI(self):

        self.parent.title('Phone List')

        menubar = Menu(self.parent)
        self.parent.configure(menu=menubar)

        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = 'File', menu=fileMenu)
        fileMenu.add_command(label='New')
        fileMenu.add_command(label='Exit', command=self.onExit)

        editMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = 'Edit', menu=editMenu)
        editMenu.add_command(label = 'Add', command=self.onAdd)
        editMenu.add_command(label = 'Change', command=self.onChange)
        editMenu.add_command(label='FInd', command=self.onFind)
        editMenu.add_command(label='Delete', command=self.onDelete)

        viewMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='View', menu=viewMenu)
        viewMenu.add_command(label='Show', command=self.onShow)
        viewMenu.add_command(label='Hide', command=self.onHide)

        frame_phone_list = Frame(self.parent)
        frame_phone_list.pack()

        self.frame_phone_list = frame_phone_list

    def onShow(self):

        try:
            PhoneList.open(PhoneList.temporarylist)
            if len(PhoneList.temporarylist) != 0:
                object_item = List(self.frame_phone_list, name='NAME', phone='PHONE')
                self.viewable_objects.append(object_item)
                for person in PhoneList.temporarylist:
                    object_item = List(self.frame_phone_list, name=person, phone=PhoneList.temporarylist[person])
                    self.viewable_objects.append(object_item)
            List.row = 0
        except EOFError:
            pass

    def onHide(self):

        for object_item in self.viewable_objects:
            object_item.remove()

    def onExit(self):

        self.quit()

    def newWindow(self):
        self.win = Toplevel(self)
        self.entry = Entry(self.win, textvariable=self.message)
        self.entry.pack(fill=BOTH)
        self.button = Button(self.win, text='Add contact', command = self.add())
        self.button.pack(fill=BOTH)

    def format_personal_info(self):

        personal_info = self.entry.get()
        personal = personal_info.split(' ')
        new_list = []
        for i in range(len(personal)):
            try:
                int(personal[i])
                number = personal[i]
                del personal[i]
                new_list.append(number)
            except ValueError:
                continue
        new_list.append(' '.join(personal))
        return new_list

    def add(self):
        personal = self.format_personal_info()

        try:
            PhoneList(personal[1], personal[0])
            PhoneList.add()
        except IndexError:
            pass

    def onAdd(self):
        self.newWindow()



    def onChange(self):
        pass

    def onFind(self):
        pass


    def onDelete(self):
        pass



root = Tk()

app = MainMenu(root)

root.mainloop()
