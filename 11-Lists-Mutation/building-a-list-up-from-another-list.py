powerball = [4, 7, 35, 46, 48, 51]

def power_of_two(numbers):
    new_string = []
    for number in numbers:
        new_string.append(number * number)
    return new_string

print(power_of_two(powerball))
print()

def convert_to_float(numbers):
    new_string_again = []
    for number in numbers:
        new_string_again.append(float(number))
    return new_string_again

print(convert_to_float(powerball))
print()

def even_or_odd(numbers):
    new_result = []
    for number in numbers:
        if number % 2 == 0:
            new_result.append(True)
        else:
            new_result.append(False)
    return new_result

print(even_or_odd(powerball))
print('----------')

# Define an only_evens function that accepts a list of numbers. 
#
# It should return a new list consisting of only the even numbers from the original list.
#
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5]) => []
# only_evens([])        => []

def only_evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))

print('----------')

# Define a long_strings function that accepts a list of strings. 
#
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# long_strings(["Hello", "Goodbye", "Sam"] => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"] => []
# long_strings([] => []

def long_strings(strings):
    more_than_5 = []
    for string in strings:
        if len(string) > 4:
            more_than_5.append(string)
    return more_than_5

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))


