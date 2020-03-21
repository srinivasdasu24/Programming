from tkinter import *
import tkinter

j = 1
speed = ['10', '20', '30', '40']
top = tkinter.Tk()
top.title('speed options')
top.geometry('200x100')

top.menubutton_1 = Menubutton(top, text='speed', relief='raised')
top.menubutton_1.menu = Menu(top.menubutton_1)
top.menubutton_1.pack()

top.user_choice = IntVar()

top.file_menu = Menu(top.menubutton_1, tearoff=0)
for i in speed:
    S = top.file_menu.add_radiobutton(label=i, variable=top.user_choice, value=i)
    j += 1
top.menubutton_1.config(menu=top.file_menu)
top.mainloop()