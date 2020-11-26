#Program: Seconds to Time
#Programmer: Jarrod Gertig (jgertig@cnm.edu)
#Purpose: Convert seconds into Weeks:Days:Hours:Minutes:Seconds

def secToTime():
    seconds = int(input("Enter the seconds: "))
    minutes = 0
    hours = 0
    days = 0
    weeks = 0
    while seconds >= 60:
        seconds -= 60
        minutes += 1
        while minutes >= 60:
            minutes -= 60
            hours += 1
            while hours >= 24:
                hours -= 24
                days += 1
                while days >= 7:
                    days -= 7
                    weeks += 1
    print(weeks,'Weeks :',days,'Days :',hours,'Hours:',minutes,'Minutes:',seconds,'Seconds\n')

while True:
    secToTime()
