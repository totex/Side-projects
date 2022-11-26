"""
Write a function isValidPassword that takes a string,
pwd as its single parameter and checks pwd to determine whether or not it is a valid password.
The function should return True if pwd is a valid password and False if it is not

A valid password has the following features

At least 1 lowercase letter from the range 'a'..'z' and 1 uppercase letter from the range 'A'..'Z'

At least 1 digit from the range '0'..'9'

At least 1 character from the set {'$','#','@'}

No other characters

Minimum length 6 characters.

Maximum length 16 characters.
"""

# letters_upper = ["A", "B", "C", "D",  "E",  "F",  "G",  "H",
#                  "I",  "J",  "K",  "L",  "M",  "N",
#                  "O",  "P",  "Q",  "R",  "S",  "T",  "U",  "V",
#                  "W",  "X",  "Y",  "Z", ]
#
# letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
#                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

import string

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)

# print("S" not in string.ascii_uppercase)


def isValidPassword3(password: str) -> bool:
    if len(password) < 6 or len(password) > 16:
        return False

    special_chars = '@#$'

    lower = 0
    upper = 0
    digit = 0
    allowed_special = 0
    not_allowed_special = 0

    for char in password:
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
        if char.isdigit():
            digit += 1
        if not char.isalnum() and char in special_chars:
            allowed_special += 1
        if not char.isalnum():
            if char in special_chars:
                allowed_special += 1
            else:
                not_allowed_special += 1

    if lower == 0 or upper == 0 or digit == 0 or allowed_special == 0 or not_allowed_special > 0:
        return False

    return True


print(isValidPassword3("p1#"))  # False - too short
print(isValidPassword3("p1234#Password5478"))  # False - too long
print(isValidPassword3("pass-W/ord@1234"))  # False - it contains not allowed chars: -/
print(isValidPassword3("paSsword#1"))  # True it contains a-zA-Z0-9@#$ and doesn't contain not allowed chars
print(isValidPassword3("paSsw#or$d"))  # False - it doesn't contain any number
print(isValidPassword3("123456789"))  # False - it contains only numbers
print(isValidPassword3("PaSsWoR$@4d"))  # True it contains a-zA-Z0-9@#$ and doesn't contain not allowed



# def isValidPassword(password: str) -> bool:
#     if len(password) < 6 or len(password) > 16:
#         return False
#
#     special_chars = '$#@'
#     # print("-" in special_chars)
#     # print("-".isalnum())
#
#     #all_bools = []
#
#     for char in password:
#         lower = False
#         upper = False
#         digit = False
#         special = False
#         if char.islower():
#             lower = True
#         if char.isupper():
#             upper = True
#         if char.isdigit():
#             digit = True
#         if not char.isalnum() and char in special_chars:
#             special = True
#
#         #all_bools.append(lower or upper or digit or special)
#
#     return lower and upper and digit and special
    #return all_bools


# print(isValidPassword("123456789"))
# print(isValidPassword("123"))
# print(isValidPassword("pass-Word@1234"))
# print(isValidPassword("paSsword#1"))
# print(isValidPassword("paSsw#or$d"))
# print(isValidPassword("PaSsWoR$@4d"))

import re

def isValidPassword2(password: str) -> bool:
    if len(password) < 6 or len(password) > 16:
        return False
    pattern = re.findall("[a-z]|[A-Z]|[0-9]|[-$#@]", password)
    print(re.search('[a-z]', password))
    print(pattern)

# isValidPassword2("123456789")
# isValidPassword2("pass-Word@12$34#")







