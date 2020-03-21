import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("condiments")
window.geometry('350x200')
menub = Menubutton(window, text='sauces', activebackground='blue')
menub.grid()
menub.menu = Menu(menub, tearoff=0)
menub["menu"] = menub.menu

mayo_sauce = IntVar()
ketchup = IntVar()
menub.menu.add_checkbutton(label='mayo', variable=mayo_sauce)
menub.menu.add_checkbutton(label='ketchup', variable=ketchup)

window.mainloop()
