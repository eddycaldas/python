# # # recursion is a funciton that call itself

# # def count_number_down(num):
# #     start = num
# #     while start > 0:
# #         print(start)
# #         start -= 1
        
# # count_number_down(5)

# # print('-----------')

# # def count_number_down2(num):
# #     if num <= 0:
# #         return
# #     else:
# #         print(num)
# #         count_number_down2(num - 1)
# #     num -= 1

# # count_number_down2(15)


# def reverse(str):
#     reverse_str = ""
#     start_index = 0
#     end_index = len(str) - 1
#     while end_index >= start_index:
#         reverse_str = reverse_str + str[end_index]
#         end_index -= 1
        
#     return reverse_str

# print(reverse("straw"))


# def reverse(str):
#     start_index = 0
#     end_index = len(str) - 1
#     reversed_string = ""
#     while end_index >= start_index:
#         reversed_string = reversed_string + str[end_index]
#         end_index -= 1

#     return reversed_string



# print(reverse("tacos al carbon"))

print('--------')

# def reverse(str):
#     start_index = 0
#     end_index = len(str) - 1
#     reversed_index = ""

#     while end_index >= start_index:
#         reversed_index = reversed_index + str[end_index]
#         end_index -= 1

#     return reversed_index



# print(reverse("quesadilla"))


# def reverse(str):
#     if len(str) <= 0:
#         return str

#     return str[-1] + reverse(str[:-1])


# print(reverse('fedex'))

# def factorial(int):
#     if int <= 1:
#         return int

#     return int * factorial(int - 1)

# print(factorial(4))
# --------------------------------->>>>>>>>


# Define a factorial function that accepts a single number

# A factorial represents the product of all numbers up to, and including, that number. For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120

# Return the factorial from your function. You should NOT use any kind of loops. Instead, utilize recursion. Your function MUST call itself.

# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120




print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))