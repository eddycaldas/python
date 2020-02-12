count = 0

while count <= 5:
    print(count)
    count += 1

print()

print(count)

print()

invalid_number = True

while invalid_number:
    user_value = int(input("Please provide a number bigger that 10: "))
    if user_value > 10:
        print(f"great!!! {user_value} is a great choice")
        invalid_number = False
    else:
        print("That number does not meet requirement, please try again")