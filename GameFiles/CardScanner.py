print("Imported CardScanner")
import numpy as np

def cardsearch():
    try:
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
                print (card1+" in location", pick[0][1],pick[0][2]+" matches "+card2+" in location", cards[k][1],cards[k][2])
                print ("card found at location", cards[k][1],cards[k][2])
                x = cards[k][1]
                y = cards[k][2]


                pickFile = open('pick.txt', 'w')
                pickFile.write("")
                pickFile.close()

                with open('cards.txt','r+') as cardFile:
                    lines = cardFile.readlines()
                    cardFile.seek(0)
                    for line in lines:
                        if card2 not in line:
                            cardFile.write(line)
                    cardFile.truncate()

                pick.remove(pick[0])#removes matches
                cards.remove(cards[k])


                return "match found",x,y
                break

            else:
                print("No match found")
                k+=1

        cards.append(pick[0])#adds the card to the array if no match is found
        for card in cards:
            print(card)

    except Exception as e:
        print("No cards in Pick.txt")
cardsearch()
