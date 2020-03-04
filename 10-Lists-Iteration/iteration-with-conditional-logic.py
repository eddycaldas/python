
# browser = "Google Chrome"
# print(browser.index('C'))
# print the sum of all odd numbers
values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odd_numbers(numbers):
    total = 0
    for i in numbers:
        if i % 2 != 0:
            total += i
    return total


print(odd_numbers(values))
print(odd_numbers(other_values))

print('--------------------------------')

# print the greatest number in a array
def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number # variable greates takes value of number because it is bigger number
    return greatest


print(greatest_number([1, 2, 3]))
print(greatest_number([3, 2, 1]))
print(greatest_number([4, 5, 5]))
print(greatest_number([-4, -1, -7]))
print('---------------------------------')

# Define a smallest_number function  that accepts a list of numbers.

# It should return the smallest value in the list.

# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))
print("---------------------------------")

# Define a function concatenate that accepts a list of strings. 

# The function should return a concatenated string which consists of all list elements whose length is greater than 2 characters.

# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => "")

def concatenate(strings):
    start_string = ""
    for i in strings:
        if len(i) > 2:
            start_string = start_string + i
    return start_string


print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"]))
print("---------------------------------")

# Write a function super_sum that accepts a list of strings. 

# The function should sum the index positions of the first occurence of the letter “s” in each word. 

# Not every word is guaranteed to have an “s”.

# Don’t use the sum keyword as it’s a built-in keyword.
#
# super_sum([]) => 0
# super_sum(["mustache"]) => 2
# super_sum(["mustache", "greatest"]) => 8
# super_sum(["mustache", "pessimist"]) => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(my_strings):
    total = 0
    for i in my_strings:
        if i.index('s'):
            total = total + i.index('s')
    return total




print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))

