errands = ["Walk Max", "Get breakfast", "Study for a bit", "Go to work"]

print(enumerate(errands))
print('-------------')

for index, task in enumerate(errands, 1):
    print(f"{task} in number {index} on my to do list for today!")

print("------------")

for index, task in enumerate(errands, 100):
    print(f"{task} in number {index} on my to do list for today!")

print('--------Excercises---------')
# Define an in_list function that accepts a list of strings and a separate string.

# Return the index where the string exists in the list. If the string does not exist, return -1.

# Do NOT use the find or index methods.

# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

def in_list(strings, string):
    for index, word in enumerate(strings):
        if word == string:
            return index
    if word != string:
        return -1


strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "love story"))

print("-----------------------")

# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0


def sum_of_values_and_indices(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total = total + (index + number)
    return total



print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))