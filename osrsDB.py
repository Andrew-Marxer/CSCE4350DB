import tkinter as tk
from tkinter import *
import sqlite3

connection = sqlite3.connect("osrs.db")

cursor1 = connection.cursor()
cursor1.execute("SELECT Monster_name FROM monster;")
names = cursor1.fetchall()
print(names)
cursor1.execute("SELECT Item_name FROM item;")
iNames = cursor1.fetchall()
class App(tk.Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        monsterMenu = Menu(menu)
        menu.add_cascade(label = "Monsters", menu=monsterMenu,)
        for mName in names:
             monsterMenu.add_command(label = mName)

        itemMenu = Menu(menu)
        menu.add_cascade(label = "Items", menu = itemMenu)
        for iName in iNames:
            itemMenu.add_command(label = iName)









root = Tk()
osrsDB = App(root)

osrsDB.master.title("Old School Runescape Monster Database")
osrsDB.master.maxsize(1000,800)

osrsDB.mainloop()

