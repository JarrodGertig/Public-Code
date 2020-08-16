print("enter a number to check if its prime")
inp = float(input())
num = int(inp)
if ((num==inp)and(num > 1)):
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
