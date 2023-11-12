from tkinter import *
import sqlite3
from instance_creator import Details

master = Tk()

connection = sqlite3.connect('Database.db')

crsr = connection.cursor()

#crsr.execute("""CREATE TABLE login (
#            username text,
#            password text,
#            last_login text
#           )""")

connection.commit()
connection.close()

master.geometry("400x300")
master.title("2FA Login")

fr1 = Frame(master)

user_name_label = Label(fr1, text = "Username: ")
user_name_label.grid(row = 0, column=0)

user_name_entry = Entry(fr1)
user_name_entry.grid(row = 0, column=1)

password_label = Label(fr1, text="Password: ")
password_label.grid(row = 1, column = 0, pady = 10)

password_entry = Entry(fr1, show = '*')
password_entry.grid(row = 1, column=1, pady = 10)

fr1.pack()

def action():
    pass

def new_login():
    new_user.config(state=DISABLED)
    window2 = Tk()
    window2.title("NEW USER LOGIN")
    window2.geometry("350x560")

    window2.mainloop()

action_button = Button(master, text = "Login!", command = action)

new_user = Button(master, text = "New User?", font = ('"Arial Light Italic" 11'), fg = '#0031f6', anchor=SE, command = new_login)
new_user.pack(side = BOTTOM, anchor = SE)

master.mainloop()