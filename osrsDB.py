import tkinter as tk
from tkinter import *
import sqlite3

connection = sqlite3.connect("osrs.db")

cursor1 = connection.cursor()
cursor1.execute("SELECT Monster_name FROM monster;")
names = cursor1.fetchall()
root = Tk()
root.title("Old School Runescape Monster Database")
root.geometry('800x800')
def search():
    return

monster_name = Entry(root,width = 50)
monster_name.grid(row = 1, column = 1, columnspan = 2, padx = 20)

monster_name_label = Label(root, text = "Enter Monster Name")
monster_name_label.grid(row = 0, column = 1)
searchButton = Button(root, text = "Click here to perform query", command = search)
searchButton.grid(row = 2, column = 1)













root.mainloop()

