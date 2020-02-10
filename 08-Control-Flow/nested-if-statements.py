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


