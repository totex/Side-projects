
feladat1 = """
Írj két függvényt:

Az első konvertáljon ceslsiusból farenheitbe.
A második konvertáljon farenheitből ceslsiusba.

A visszadott értékek egy tizedes számot tartalmazzanak.

A két formula: 

f = c × 9/5 + 32
c = (f - 32) * 5/9

f = farenheit
c = celsius 

>>>cel_to_far(30)
86
>>>cel_to_far(40)
104

>>>far_to_cel(30)
-1.1
>>>far_to_cel(40)
4.4

"""

# celsius to fahrenheit
def cel_to_far(c):
    return c * 9/5 + 32

print(cel_to_far(30))
print(cel_to_far(40))


# fahrenheit to celsius
def far_to_cel(f):
    return round((f - 32) * 5/9, 1)

print(far_to_cel(30))
print(far_to_cel(40))







