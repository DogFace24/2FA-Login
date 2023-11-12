from tkinter import *

master = Tk()

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

master.mainloop()