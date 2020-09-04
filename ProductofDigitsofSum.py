#Product of Digits of Sum
#Programmer: Jarrod Gertig
#Date: Sept. 4, 2020

#Main math function
def funny_func(a,args):         # To get the Product of Digits of Sum:
    for arg in args:            #    for each number
        a += arg                #      add them all to the first number
    spread = list(str(a))       #    make a list of digits in the sum
    beta = 1                    #    multiplier of 1
    for letter in spread:       #    for each digit    
        beta *= int(letter)     #       multiply all the digits
    while len(str(beta))>1:     #    while digit count is > 1
        delta = list(str(beta)) #       make new list of digits
        beta = 1                #       multiplier
        for letter in delta:    #       for each digit
            beta *= int(letter) #          multiply
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
