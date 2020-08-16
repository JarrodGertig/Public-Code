print("enter a number to check if its prime")
inp = float(input())                         #Get raw numerical input
num = int(inp)                               #Turn into integer
if ((num==inp)and(num > 1)):                 #If float=integer, meaning decimal wasn't input, and its greater than 1
   for i in range(2,(int(num/2)+1)):         #for range 2 to half the number
       if (num % i) == 0:                    #if the number is divisible with a 0 zero remainder
           print(num,"is not a prime number")#its not prime
           print(i,"times",num//i,"is",num)  #read the factors
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
