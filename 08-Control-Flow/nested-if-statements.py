ingredient1 = 'pasta'
ingredient2 = 'meatballs'

if ingredient1 == 'pasta':
    if ingredient2 == 'meatballs':
        print('make some pasta with meatballs')
    else:
        print('make plain pasta')
else:
    print('I have no recommendation')

print()

if ingredient1 == 'pasta' and ingredient2 == 'meatballs':
    print('make some pasta with meatballs')
elif ingredient1 == 'pasta':
    print('make plain pasta')
else:
    print('I have no recommendation')

print()

# Define a divisible_by_three_and_four function 
# that accepts a number as its argument. 
# It should return True if the number is evenly 
# divisible by both 3 and 4 . It should return False otherwise.

# divisible_by_three_and_four(3) => False
# divisible_by_three_and_four(4) => False
# divisible_by_three_and_four(12) => True
# divisible_by_three_and_four(18) => False
# divisible_by_three_and_four(24) => true

def divisible_by_three_and_four(num):
    if (num % 3 == 0) and (num % 4 == 0):
        print(True)
    else:
        print(False)

divisible_by_three_and_four(3)
divisible_by_three_and_four(4)
divisible_by_three_and_four(12)
divisible_by_three_and_four(18)
divisible_by_three_and_four(24)

print()

# Declare a string_theory function that accepts 
# a string as an argument. 

# It should return True if the string has 
# more than 3 characters and starts with a 
# capital “S”. It should return False otherwise.

# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

def string_theory(str): 
    if len(str) > 3 and str[0] == 'S':
        print(True)
    else:
        print(False)

string_theory("Sansa")
string_theory("Story")
string_theory("See")
string_theory("Fable")