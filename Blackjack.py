#Blackjack
#Programmer: Jarrod Gertig
#Date: September 9, 2020
#play blackjack

def blackjack(cards):               # Blackjack function
    i = 0                               # card sum variable
    a = 0                               # ace count variable
    for x in range(len(cards)):         # check each card in hand
        if cards[x] in ['K','Q','J']:   #    if its a facecard
            i += 10                     #       add 10
        elif cards[x] == 'A':           #    if its an ace
            a += 1                      #       count up aces
        else:                           #    if its a number
            i += int(cards[x])          #       add it in
    if a > 0:                           # if aces were in hand
        for x in range(a-1):            #    for all but one ace
            i += 1                      #       add 1 to hand sum
        if i > 10:                      #    for last ace, if hand sum more than 10
            i += 1                      #       add low Ace 1
        else:                           #    if hand sum 10 or less
            i += 11                     #       add high Ace 11
    print("Your cards add up to "+str(i))
    if i <= 21:                         # if hand sum is 21 or less
        return False                    #    return False
    else:                               # if hand sum over 21
        return True                     #    return True

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
