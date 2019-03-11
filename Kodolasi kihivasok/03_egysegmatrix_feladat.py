
feladat3 = """
Írj egy függvényt, ami egy egységmátrixot generál (identity matrix).
Ez a matrix minding legyen negyzetes pl: 4x4, 5x5, 10x10 stb.
Tehat a sorok es oszlopok szama legyen mindig egyenlo. 

pl 4x4:
matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

Pseudo kód:
függvény definíció(dim) # dim = dimenzio
    mátrix lista []
    külső ciklus y (dim)
        valahányszor a külső ciklus lefut, a mátrix listához hozzáadunk egy üres belső listát [[]]
        belső ciklus x (dim)
            ha y modulo dim == x és x modulo dim == x:
                matrix listába az y indexnél, hozzáadunk (append) egy egyest
            egyébként meg:
                matrix listába az y indexnél, hozzáadunk (append) egy nullát
    
    végül visszadjuk a mátrix listát
        

>>m = matrix_identity(4)
>>print(m)
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

Majd írj egy függvényt, ami kiírja a konzolra a mátrixot sorról sorra.

>>matrix_print(m)
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]

Az első függvény neve legyen: matrix_identity
A második függvény neve legyen: matrix_print

"""



