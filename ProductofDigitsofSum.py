#Product of Digits of Sum
#Programmer: Jarrod Gertig
#Date: Sept. 4, 2020
#

def funny_func(a,args):
    for arg in args:
        a += arg
    spread = list(str(a))
    print(spread)
    beta = 1
    for letter in spread:
        beta *= int(letter)
    while len(str(beta))>1:
        delta = list(str(beta))
        print(delta)
        beta = 1
        for letter in delta:
            beta *= int(letter)
    print(beta)

def injector():
    first = int(input("Enter the first number: "))
    numbers = []
    marker = True
    while marker:
        holder = input("Enter another number (leave blank if done): ")
        if holder == '':
            marker = False
        else:
            numbers.append(int(holder))
    funny_func(first,numbers)

injector()
