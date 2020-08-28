from math import *
while True:
    print("Enter the coefficients for ax^2+bx+c=0:\nEnter a")
    a=float(input())
    print("Enter b")                #Get all the inputs
    b=float(input())
    print("Enter c")
    c=float(input())
    if a!=0:                                            # a!=0 means no division by 0
        if ((b**2)-(4*a*c))>=0:                         # if thats>=0 then sqrt works fine
            xplus=((-1*b)+sqrt((b**2)-(4*a*c)))/(2*a)   # Quadratic Formula
            xmins=((-1*b)-sqrt((b**2)-(4*a*c)))/(2*a)   # Second Root
            print("Root1: %.3f | Root2: %.3f\n"%(xplus,xmins))
        else:                                           # if its <0 then sqrt is imaginary
            root=sqrt(abs((b**2)-(4*a*c)))              
            preb=-1*b
            twoa=2*a                                    # Print imaginary roots
            print("Root1: (%.3f + %.3fi)/%.3f | Root2: (%.3f - %.3fi)/%.3f\n"%(preb,root,twoa,preb,root,twoa))
    elif b==0:
        if c==0:
            print("Is this a joke to you?\n") # a=b=c=0 case
        else:
            print("%.3f is not equal to zero... idk how you got those values\n"%c) # a=b=0, thus c should equal 0
    else:
        print("You've entered values for a linear equation | Root: %.3f\n"%((-1*c)/b)) # a=0, thus bx+c=0
