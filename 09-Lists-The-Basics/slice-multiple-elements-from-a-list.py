print('programming'[3:7])

colors = ['blue', 'black', 'red', 'orange']

print(colors[2:4])
print(colors[:3])

print()
print(colors[::2])
print(colors[::-1])

print()

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3) => ["a", "b"]
# split_in_two(values, 4) => ["c", "d", "e", "f"]
# split_in_two(values, 1) => ["a", "b"]
# split_in_two(values, 10) => ["c", "d", "e", "f"]

values = ['a', 'b', 'c', 'd', 'e', 'f']

def split_in_two(values, n):
    # values = ['a', 'b', 'c', 'd', 'e', 'f']
    if (n % 2 == 0):
        return values[2:]
    else:
        return values[:2]

print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))

print('----------')

# Declare a nested_extraction function that accepts a list of lists and an index position.

# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position

# You can assume the number of lists will always be equal to 
# the number of elements within each of them.

# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0) => # 3
# nested_extraction(nl, 1) => # 8
# nested_extraction(nl, 2) => # 12

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]

def nested_extraction(nl, index):
    return nl[index][index]

print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))

print('-----------')

# Declare a beginning_and_end function that accepts a list of elements.

# It should return True if the first and last elements in the list are equal and False if they are unequal.

# Assume the list will always have at least 1 element.

# beginning_and_end([1, 2, 3, 1])    => True
# beginning_and_end([1, 2, 3, 4, 5]) => False
# beginning_and_end(["a", "b", "a"]) => True
# beginning_and_end([15])            => True

def beginning_and_end(my_list):
    if (my_list[0] == my_list[-1]):
        return True
    else:
        return False

print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))
print(beginning_and_end(["a", "b", "a"]))
print(beginning_and_end([15]))

print('-------------')

# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the word exists in the list AND
#   - the word has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

words = ["cat", "dog", "rhino"]

def long_word_in_collection(words, str):
    if (str in words and len(str) >= 4):
        return True
    else:
        return False

print(long_word_in_collection(words, "rhino"))
print(long_word_in_collection(words, "cat"))
print(long_word_in_collection(words, "monkey"))