from tkinter import *

# 1 km = 1/1.609344 mi
def km_to_mi():
    try:
        km = bemenet1.get()
        ktm = float(km) / 1.609344
        text1['state'] = NORMAL
        text1.delete(1.0, END)
        ktm = str(ktm)
        text1.insert(END, ktm[0:5])
        text1['state'] = DISABLED
    except:
        text1['state'] = NORMAL
        text1.delete(1.0, END)
        text1.insert(END, 'Csak szamokat!')
        text1['state'] = DISABLED


# f = c * 9/5 + 32
def cel_to_far():
    try:
        cel = bemenet2.get()
        ctf = float(cel) * 9/5 + 32
        text2['state'] = NORMAL
        text2.delete(1.0, END)
        ctf = str(ctf)
        text2.insert(END, ctf[0:5])
        text2['state'] = DISABLED
    except:
        text2['state'] = NORMAL
        text2.delete(1.0, END)
        text2.insert(END, 'Csak szamokat!')
        text2['state'] = DISABLED

# az alap ablak
win = Tk()
# az ablak neve/cime
win.title('Konverter')
# az ablak merete
win.geometry('800x600')

# text/szoveg/cimke
Label(win, text="kilométer", font="Helvetica 12 bold").grid(row=0, column=1)
Label(win, text="mérföld", font="Helvetica 12 bold").grid(row=1, column=1)

Label(win, text="celsius", font="Helvetica 12 bold").grid(row=3, column=1)
Label(win, text="fahrenheit", font="Helvetica 12 bold").grid(row=4, column=1)

# gomb, a lenyomasaval vegrehajtodik a szamitas
Button(win, text="calculate km to mi", command=km_to_mi, font="Helvetica 12 bold").grid(row=2, column=0)
Button(win, text='calculate c to f', command=cel_to_far, font="Helvetica 12 bold").grid(row=5, column=0)

# ide irjuk be a kilometert szamokban
bemenet1 = Entry(win, font="Helvetica 20 bold")
bemenet1.grid(row=0, column=0)

# ide irjuk be a celsiust szamokban
bemenet2 = Entry(win, font="Helvetica 20 bold")
bemenet2.grid(row=3, column=0)

# itt fog mejelenni a szamitas mint merfold
text1 = Text(win, height=1, width=20, state=DISABLED, font="Helvetica 20 bold")
text1.grid(row=1, column=0)

# itt fog mejelenni a szamitas mint farenheit
text2 = Text(win, height=1, width=20, state=DISABLED, font="Helvetica 20 bold")
text2.grid(row=4, column=0)

# fo applikacio ciklus
win.mainloop()