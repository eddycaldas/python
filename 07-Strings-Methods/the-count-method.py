# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")     => 3
# vowel_count("helicopter") => 4
# vowel_count("ssh")        =>

def vowel_count(str):
    print(str.count('a') +
          str.count('e') +
          str.count('i') +
          str.count('o') +
          str.count('u')  )

vowel_count("estate")
vowel_count("helicopter")
vowel_count("ssh")
print()
print()
print()
#  -------------------------------------->

# Define a find_my_letter function that accepts 
# two arguments: a string and a character
# The function should return the first index position 
# of the character in the string
# The function should return a -1 if the character 
# does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a") => 1
# find_my_letter("bazooka", "z") => 2
# find_my_letter("lollipop", "z") => -1

def find_my_letter(str, x):
    print(str.find(x))

find_my_letter("dangerous", "a")
find_my_letter("bazooka", "z")
find_my_letter("lollipop", "z")