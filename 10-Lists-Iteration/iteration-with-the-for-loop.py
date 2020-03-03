dinner = 'steak with potatoes'

# for i in dinner:
#     print(i)

comidas = ['ceviche', 'saltado', 'papitas fritas']

for i in comidas:
    print(i)
    print(len(i))
print('------')

numbers = [1, 4, 7, 23, 45]

for i in numbers:
    print(i * 2)

print('----------')

total = 0
for i in numbers:
    total = total + i

print(total)

print("==================")

# Define a sum_of_lengths function that accepts a list of strings.

# The function should return the sum of the string lengths.

# sum_of_lengths(["Hello", "Bob"]) => 8
# sum_of_lengths(["Nonsense"])     => 8
# sum_of_lengths(["Nonsense", "or", "confidence"]) => 20

def sum_of_lengths(str):
    total_length = 0
    for i in str:
        total_length = total_length + len(i)
    return total_length

print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]))

print('----------')

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# product([1, 2, 3]) => 6
# product([4, 5, 6, 7]) => 840
# product([10]) => 10

def product(my_values):
    initial_total = 1
    for i in my_values:
        initial_total = initial_total * i
    return initial_total


print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))