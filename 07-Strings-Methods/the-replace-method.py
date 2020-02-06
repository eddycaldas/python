my_number = '555 455 5555'
print(my_number.replace(' ', '-'))
print(my_number.replace('5', '9'))

# Define a fancy_cleanup function that accepts a 
# single string argument
# The function should clean up the whitespace on 
# both sides of the
# argument. It should also replace every occurence 
# of the letter "g" with the
# letter "z" and every occurence of a space with 
# an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ") => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ") => "nonsense"
# fancy_cleanup("grade") => "zrade"
print()

def fancy_cleanup(str):
    print(str.strip().replace('g', 'z').replace(' ', '!'))

fancy_cleanup("       geronimo crikey  ")
fancy_cleanup("       nonsense  ")
fancy_cleanup("grade")