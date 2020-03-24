
from tkinter import *
from tkinter import ttk
from db_manager import *

win = Tk()
win.title("Adatbazis demo")
win.geometry("1020x640")
win.resizable(False, False)

db_create()

Label(win, text="name", font="Helvetica 12 bold").grid(row=0, column=0)
name = Entry(win, font="Helvetica 20 bold")
name.grid(row=0, column=1, padx=5, pady=5)

Label(win, text="age", font="Helvetica 12 bold").grid(row=1, column=0)
age = Entry(win, font="Helvetica 20 bold")
age.grid(row=1, column=1, padx=5, pady=5)

Label(win, text="gender", font="Helvetica 12 bold").grid(row=2, column=0)
gender = StringVar(win)
gender.set("select your gender")
genders = OptionMenu(win, gender, "male", "female")
genders.grid(row=2, column=1, padx=5, pady=5)

Label(win, text="score", font="Helvetica 12 bold").grid(row=3, column=0)
score = Entry(win, font="Helvetica 20 bold")
score.grid(row=3, column=1, padx=5, pady=5)

Button(win, text="insert data", command=lambda: db_insert(name, age, gender, score), font="Helvetica 12 bold").grid(row=4, column=0, columnspan=2, padx=5, pady=5)

cols = ("Id", "Name", "Age", "Gender", "Score")
table = ttk.Treeview(win, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
table.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

Button(win, text="query data", command=lambda: db_query(table), font="Helvetica 12 bold").grid(row=6, column=0, columnspan=2, padx=5, pady=5)
Button(win, text="export to CSV", command=db_export_csv, font="Helvetica 12 bold").grid(row=7, column=0, columnspan=2, padx=5, pady=5)

win.mainloop()
db_close()

