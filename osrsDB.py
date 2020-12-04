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
    connection = sqlite3.connect("osrs.db")
    cursor1 = connection.cursor()

    result = ""
    result_label['text'] = ""
    result_label.grid(row=3, column=1, pady=20)
    cursor1.execute("""SELECT * FROM drops NATURAL JOIN monster WHERE monster.Monster_name = ?""",[monster_name.get()])
    records = cursor1.fetchall()

    for record in records:
        result += "Item: " +str(record[3])+"  Drop Rate: 1/"+str(record[0]) + " Item Price: " + str(record[1]) + '\n'

    result_label['text'] = result

    connection.commit()
    connection.close()
    return
monster_name = Entry(root, width = 50)
monster_name.grid(row = 1, column = 1, columnspan = 2, padx = 20)

monster_name_label = Label(root, text = "Enter Monster Name")
monster_name_label.grid(row = 0, column = 1)
searchButton = Button(root, text = "Click here to perform query", command = search)
searchButton.grid(row = 2, column = 1)

result_label = Label(root, text = "")
result_label.grid(row=3, column=1, pady=20)

fileName = PhotoImage(file = "C:\\Users\\Andy\\Downloads\\osrs.png")
imageLabel = Label(root, image = fileName)
imageLabel.place(x = 150, y = 200, relwidth = 1, relheight = 1)

root.mainloop()

