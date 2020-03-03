
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

print('------')

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
