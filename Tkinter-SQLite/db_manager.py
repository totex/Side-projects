import sqlite3

conn = None
curs = None

def db_create():
    global conn, curs
    conn = sqlite3.connect("users/data2.db")
    curs = conn.cursor()

    curs.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, gender TEXT, score REAL)")


def db_insert(name, age, gender, score):
    if not name.get() or not age.get() or gender.get() == "select your gender" or not score.get():
        print("Az osszes mezo kitoltese kotelezo!!!")
        return

    curs.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (name.get(), age.get(), gender.get(), score.get()))
    conn.commit()

    name.delete(0, 'end')
    age.delete(0, 'end')
    score.delete(0, 'end')

def db_query(table):
    curs.execute("SELECT * FROM users")
    datas = curs.fetchall()

    table.delete(*table.get_children())

    rowid = 1
    for data in datas:
        table.insert("", "end", values=(rowid, data[0], data[1], data[2], data[3]))
        rowid += 1

def db_export_csv():
    curs.execute("SELECT * FROM users")
    datas = curs.fetchall()
    with open("users/data.csv", "w", encoding="utf-8") as out_file:
        out_file.write(";".join(["name", "age", "gender", "score"]))
        out_file.write("\n")
        for data in datas:
            out_file.write(";".join(str(d) for d in data))
            out_file.write("\n")

def db_close():
    if conn and curs:
        print("Adatbazis lezarva.")
        curs.close()
        conn.close()
