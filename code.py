x = 0
y = 0

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
        #print (cards[k][0])
       
        card1 = pick[0][0]
        card2 = cards[k][0]
        if card1 == card2:
            #print ("card matches")
            #print ("card found at location", cards[k][1],cards[k][2])
            x = cards[k][1]
            y = cards[k][2]
            #print (x,y)
            return 1
            break
        else:
            cards[k][0]
            print("card not match " + str(k))
            k+=1

playerOne = str(input("Please enter player one name: "))
playerTwo = str(input("Please enter player two name: "))
playerOneScore = 0
playerTwoScore = 0

while True:
  if playerOneScore < 6 and playerTwoScore < 6:
    resultOne = cardsearch()
    if resultOne == 1:
      playerOneScore += 1
      print(playerOne,"'s score: ",playerOneScore)
    else:
      print("No match, player Twos turn")
 
  if playerOneScore < 6 and playerTwoScore < 6:
    resultTwo = cardsearch()
    if resultTwo == 1:
      playerTwoScore += 1
      print(playerTwo,"'s score: ",playerTwoScore)
    else:
      print("No match, player Ones turn")

  elif playerOneScore == 6 or playerTwoScore == 6:
    print("Game over!")
    break

if playerOneScore == 6:
  print(playerOne," wins!")
else:
  print(playerTwo," wins!")
 
