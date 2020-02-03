content = '      tacos          '

print(content.lstrip())
print(len(content.lstrip()))
print()

print(content.rstrip())
print(len(content.rstrip()))
print()

print(content.strip())
print(len(content.strip()))
print()

website = 'www.python.org'
print(website.lstrip('w'))
print(website.rstrip('.org'))
print((website.strip('worg.')))

# it focus on removing characters fromt he beggining
# of the string or the end.