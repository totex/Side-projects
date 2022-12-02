
def isDivisibleBy(num1: int, num2: int):
    return num1 % num2 == 0


def fizzBuzz(n: int) -> str:
    if isDivisibleBy(n, 3) and isDivisibleBy(n, 5):
        result = "FizzBuzz"
    elif isDivisibleBy(n, 3):
        result = "Fizz"
    elif isDivisibleBy(n, 5):
        result = "Buzz"
    else:
        result = ""
    
    return result


def playFB():
    num = int(input("Please enter a number: "))
    if num < 1:
        print("Number has to be greater than 0!")
        num = int(input("Please type a new number: "))
    for i in range(1, num+1):
        print(i, fizzBuzz(i))
    
    
playFB()

##numbers = list(range(20))
##
##for n in numbers:
##    print(fizzBuzz(n))


"""
##def fizzBuzz(n: int) -> str:
##    if n % 3 == 0 and n % 5 == 0:
##        return "FizzBuzz"
##    elif n % 3 == 0:
##        return "Fizz"
##    elif n % 5 == 0:
##        return "Buzz"
##    
##    return "Bla"

"""

    

