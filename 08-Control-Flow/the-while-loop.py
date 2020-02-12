# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print()

# print(count)

# print()

# invalid_number = True

# while invalid_number:
#     user_value = int(input("Please provide a number bigger that 10: "))
#     if user_value > 10:
#         print(f"great!!! {user_value} is a great choice")
#         invalid_number = False
#     else:
#         print("That number does not meet requirement, please try again")

print()
print()

# FizzBuzz is a popular programming problem to test a developer's ability 
# to think logically with code.

# The problem is simple but deceptive.

# Define a fizzbuzz function that accepts a single number as an argument. 
# The function should print every number from 1 to that argument. 

# There are a couple caveats.

# If the number is divisible by 3, print "Fizz" instead of the number.

# If the number is divisible by 5, print "Buzz" instead of the number.

# If the number is divisible by both 3 and 5, print "FizzBuzz" 
# instead of the number.

# If the number is not divisible by either 3 or 5, just print the number.

# Example: fizzbuzz(30)should print:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz

def fizzbuzz(num):
    count = 1
    while count <= num:
        if (count % 3 == 0 and count % 5 == 0):
            print("FizzBuzz")
        elif count % 3 == 0:
            print ('Fizz')
        elif count % 5 == 0:
            print('Buzz')
        else:
            print(count)
        
        
        count += 1


fizzbuzz(30)