#Blackjack
#Programmer: Jarrod Gertig
#Date: September 9, 2020
#play blackjack

def blackjack(cards):
    i = 0
    a = 0
    for x in range(len(cards)):
        if cards[x] in ['K','Q','J']:
            i += 10
        elif cards[x] == 'A':
            a += 1
        else:
            i += int(cards[x])
    if a > 0:
        for x in range(a):
            if i <= 10:
                i += 11
            else:
                i += 1
    print("Your cards add up to "+str(i))
    if i <= 21:
        return False
    else:
        return True

def runner():
    data = input("Please enter a card series: ")
    if data == 'Z':
        return False
    hand = []
    for i in range(len(data)):
        hand.append(data[i])
    if blackjack(hand):
        print("Ouch, you blew it...\n")
    else:
        print("Congratulations partner, you done won it!\n")
    return True

loopsRun=0
print("When entering a card series, use the following format:\nIf you want: King, Jack, & Six  or:  Queen, Nine, Ace, & Two\nThen enter:  KJ6                or:  Q9A2\nTo exit, enter the key character: Z\n")
while runner():
    loopsRun+=1
print("Thank you for playing blackjack, you played %d hands."%(loopsRun))
