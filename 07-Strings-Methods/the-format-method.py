
# # name, adjective, noun
# mad_libs = "{} laugh at the {} {}."
# print(mad_libs.format('Bobby', 'green', 'alien'))
# print()

# mad_libs = "{2} laugh at the {1} {0}."
# print(mad_libs.format('Bobby', 'green', 'alien'))
# print()

# mad_libs = "{name} laugh at the {adjective} {noun}."
# print(mad_libs.format(name = 'Bobby', adjective = 'green', noun = 'alien'))

# mad_libs = "{name} laugh at the {adjective} {noun}."

# name = input("Enter a name: ")
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")

# print(mad_libs.format(name = name, adjective = adjective, noun = noun))

# this gets performed on a terminal

about_me = "I was born in {country}, which is in {continent} on {month}."

country = input("Country born: ")
continent = input("which continent: ")
month = input("month born: ")

print(about_me.format(country = country, continent = continent, month = month))
