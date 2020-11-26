#Program: Hours to Seconds
#Programmer: Jarrod Gertig (jgertig@cnm.edu)
#Purpose: Convert Hours into seconds

def hourToSec():
    hours = float(input("Enter the hours: "))
    seconds = 3600*hours
    print(hours,'hours is equal to',seconds,'seconds')

while True:
    hourToSec()
