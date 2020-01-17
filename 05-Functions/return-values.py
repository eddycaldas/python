# Define a convert_to_currency function that accepts 
# a single parameter (an integer). 
# The function should convert the argument to a string, 
# prefix it with a dollar sign, and return the result.
# Example: convert_to_currency(15) => "$15"

def convert_to_currency(x):
    m = int(x)
    n = "$" + str(m)
    print('"' + n +  '"')

convert_to_currency(15)
