#Product of Digits of Sum
#Programmer: Jarrod Gertig
#Date: Sept. 4, 2020
#

#Main math function
def funny_func(a,args):         # To get the Product of Digits of Sum:
    beta = a                    #    beta is placeholder for sum and products
    for arg in args:            #    for each number
        beta += arg             #      add it to the summation
    while len(str(beta))>1:     #    while digit count is > 1
        delta = list(str(beta)) #       make new list of digits
        beta = 1                #       multiplier
        for digit in delta:     #       for each digit
            beta *= int(digit)  #          multiply
    print(beta)                 #    When only one digit remains, print it.

#Function to get effective inputs
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
