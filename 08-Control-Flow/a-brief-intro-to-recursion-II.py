# recursion is a funciton that call itself

def count_number_down(num):
    start = num
    while start > 0:
        print(start)
        start -= 1
        
count_number_down(5)

print('-----------')

def count_number_down2(num):
    if num <= 0:
        return
    else:
        print(num)
        count_number_down2(num - 1)
    num -= 1

count_number_down2(15)