errands = ["Walk Max", "Get breakfast", "Study for a bit", "Go to work"]

print(enumerate(errands))
print('-------------')

for index, task in enumerate(errands, 1):
    print(f"{task} in number {index} on my to do list for today!")

print("------------")

for index, task in enumerate(errands, 100):
    print(f"{task} in number {index} on my to do list for today!")