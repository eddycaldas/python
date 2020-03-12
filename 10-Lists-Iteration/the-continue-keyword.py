def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value > 0:
            total += value
    return total

print(sum_of_positive_numbers([1, 2, -3, 4]))

print('----------')

def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value < 0:
            continue
        total += value
    return total

print(sum_of_positive_numbers([1, 2, -3, 4]))

print('----------')

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0

def length_match(strings, num):
    total = 0
    for string in strings:
        if len(string) == num:
            total += 1
    return total

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([], 5))

print('----------')

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# sum_from(1, 2)   # 1 + 2 => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5 => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8 => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12 => 42

def sum_from(smaller, bigger):
    total = 0
    if bigger > smaller:
        for num in range(smaller, bigger + 1):
            total += num
    return total

print(sum_from(1, 2))
print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12)) 

print('----------')

# Declare a function same_index_values that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# same_values([1, 2, 3], [3, 2, 1]) => [1]
# same_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) => [1, 3]

