# using while loop
def countInCubes1(n: int):
    counter = 1
    while counter < n+1:
        cube = pow(counter, 3)
        print(cube)
        counter += 1

# using for loop
def countInCubes2(n: int):
    for i in range(1, n+1):
        cube = pow(i, 3)
        print(cube)


countInCubes1(5)
print("--------")
countInCubes2(5)
