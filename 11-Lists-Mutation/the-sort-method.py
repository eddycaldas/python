# sorts a list in place
# if list is numeric, the list will be sorted in ascending order
# if list is alphabetical order, it'll be sorted on alphabetical order
#capital letters get sorted before lower case letters

temperatures = [32, 4, 73, 65, 26]
temperatures.sort()
print(temperatures)

print()
numbers = [9, 32, 24, 98, 45]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print('------------')

coffees = ['latte', 'black', 'frapucchino', 'nose']
coffees.sort()
print(coffees)

coffees.reverse()
print(coffees)

print("-------")

numbers = [1, 4, 5, 7, 9]

# how can you overwrite the values 4 and 5 with 6 and 8?

numbers.remove(1)
numbers.remove(7)
numbers.remove(9)
numbers.append(6)
numbers.append(8)
print(numbers)
