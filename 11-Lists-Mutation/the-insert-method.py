# insert method allows to insert a list int hemiddle or the beggining of the list. it takes two arguments; index and object

cars = ['toyota', 'honda', 'bmw']

cars.insert(1, 'subaru')

print(cars)

print('----------')

# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(number):
    start_number = 1
    my_list = []
    for num in range(start_number, number + 1):
        if number % num == 0:
            my_list.append(num)
    return my_list

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))
