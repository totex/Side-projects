
feladat2 = """
Írj egy függvényt, ami egy 2 dimenziós rácsos szerkezetet hoz létre (grid).
A függvénynek két bemeneti paramétere legyen: row, column (sor, oszlop)
Töltsd ki ezt a rácsot csupa nullával.

Pseudo kód:
függvény definíció(row, column)
    rács lista []
    külső ciklus y (row)
        rács listához hozzádunk egy belső üres listát
        belső ciklus x (column)
            a rács lista belső listájába (rács lista az y indexnél), hozzáadunk egy nullát
            
    végül visszadjuk a rács listát


>>>g = grid_create(5, 5)
>>>print(g)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

Majd definiálj még egy függvényt, ami egy rács bementet fogad, és kiírja ezt a rácsot a konzolra, sorról sorra.

>>>grid_print(g)
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]

Az első függvény neve legyen: grid_create
A második függvény neve legyen: grid_print

"""
