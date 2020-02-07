# # zero or empty string are falsie values, all other numbers are not

# if 3:
#     print('Yes!')

# if 0:
#     print("humm...")

# print()

# print(bool(0))
# print(bool(-1))
# print(bool(""))
# print(bool(" "))

# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2) => "even"
# even_or_odd(0) => "even"
# even_or_odd(13) => "odd"
# even_or_odd(9) => "odd"

def even_or_odd(int):
    if (int%2 == 0):
        print("even")
    elif (int%2 != 0):
        print('odd')

even_or_odd(2) 
even_or_odd(0) 
even_or_odd(13) 
even_or_odd(9) 

print()

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either truthy or falsy.
# 
# truthy_or_falsy(0) => "The value 0 is falsy"
# truthy_or_falsy(5) => "The value 5 is truthy"
# truthy_or_falsy("Hello") => "The value Hello is truthy"
# truthy_or_falsy("") => "The value  is falsy"

def truthy_or_falsy(arg):
    if arg == 0 or arg == '':
        print("The value ", arg, ' is falsy' )
    else:
        print('The value ', arg, ' is truthy')

truthy_or_falsy(0)
truthy_or_falsy(5)
truthy_or_falsy("Hello")
truthy_or_falsy("")