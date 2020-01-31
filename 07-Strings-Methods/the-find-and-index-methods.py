browser = "Google Chrome"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))

print('\n')

print(browser.find("R"))

#  -1 means that the character or string is not
#  on the original string itself
# ---------------------------->
print()

print(browser.find('o', 2))
print(browser.find('o', 5))

# in this case, a second argument is where the
# search of the character or string starts.

# ----------------------------->
print()

print(browser.index('C'))
print(browser.index("Z"))

# index method is the same as the find one, 
# but instead it'll return a ValueError instead 
# of the -1 as the find method does.