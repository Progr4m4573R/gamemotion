print("Imported CardScanner")
import numpy as np

x = 0
y = 0
found = False# becomes true when a card is found

def cardsearch():
    pick = []#Card We are sent by open cv(ONE AT A TIME)
    cards = []#Cards we have seen

    i = 0
    with open('cards.txt', 'r') as openfile:
        for line in openfile:
            cards.append([])
            cards[i] = [str(n) for n in line.split(',')]
            i += 1


    j = 0
    with open('pick.txt', 'r') as openfile:
        for line in openfile:
            pick.append([])
            pick[j] = [str(n) for n in line.split(',')]
            j += 1

    k = 0
    for k in range(len(cards)):
        print (cards[k][0])
        
        card1 = pick[0][0]
        card2 = cards[k][0]
        if card1 == card2:
            print ("card matches")
            print ("card found at location", cards[k][1],cards[k][2])
            x = cards[k][1]
            y = cards[k][2]
            print (x,y)
            found = True
            break
        else:
            cards[k][0]
            print("card not match " + str(k))
            k+=1

cardsearch()

