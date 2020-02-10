# def positive_or_negative(num):
#     if num > 0:
#         print("Positive!")
#     elif num < 0:
#         print("Negative!")
#     else:
#         print("neither, it is a zero")

# positive_or_negative(4)
# positive_or_negative(-3)
# positive_or_negative(0)


# Define an up_and_down function that accepts a string argument
# If the string consists of all uppercase letters, return a new string
# consisting of all lowercase letters. If the string consists of all
# lowercase letters, return a new string consisting of all uppercase
# characters. If the string has a mix of uppercase and lowercase
# characters, return a new string where the casing of each 
# letter is swapped.
# 
# up_and_down("HELLO") => "hello"
# up_and_down("genius") => "GENIUS"
# up_and_down("ESPreSso") => "espREsSO"

def up_and_down(str):
    if str == str.upper():
        print(str.lower())
    elif str == str.lower():
        print(str.upper())
    else:
        print(str.swapcase())

up_and_down("HELLO")
up_and_down("genius")
up_and_down("ESPreSso")
print()

# Declare a negative_energy function that accepts 
# a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5) => 5
# negative_energy(10) => 10
# negative_energy(-5) => 5
# negative_energy(-8) => 8
# negative_energy(0) => 0

def negative_energy(num):
    if num > 0:
        print(num)
    elif num < 0:
        print(-num)
    else:
        print(0)


negative_energy(5)
negative_energy(10)
negative_energy(-5)
negative_energy(-8)
negative_energy(0)