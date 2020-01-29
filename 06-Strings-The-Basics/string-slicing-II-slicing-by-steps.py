alphabet = "abcdefghijklmnopqrstuvwxy"

print(alphabet[3:12])
print(alphabet[:12:2])
print(alphabet[::2])

print('\n')

print(alphabet[-23:-8:5])

print('\n')

print(alphabet[::-2])
print(alphabet[::-1])

# ----------------------------------------

# Define a first_three_characters function that 
# accepts a string argument.
# The function should return the first 3 characters 
# of the string.
#
# EXAMPLES:
# first_three_characters("dynasty") => "dyn"
# first_three_characters("empire")  => "emp"

def first_three_characters(str):
    return str[:3]

print(first_three_characters("dynasty"))
print(first_three_characters("empire"))

#  --------------------------------

# Define a last_five_characters function 
# that accepts a string argument. 
# The function should return the last 
# 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty") => "nasty"
# last_five_characters("empire") => "mpire"

def last_five_characters(str):
    return str[-5::1]

print(last_five_characters("dynasty"))
print(last_five_characters("empire"))

# ------------------------------------

# Define a is_palindrome function that 
# accepts a string argument. 
# The function should return True if the 
# string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar") => True
# is_palindrome("yummy")   => False

def is_palindrome(str):
    if str[:] == str[::-1]:
        return True
    elif str[:] != str[::-1]:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))


