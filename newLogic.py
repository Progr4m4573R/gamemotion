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
            print ("card matches")
            #print ("card found at location", cards[k][1],cards[k][2])
            x = cards[k][1]
            y = cards[k][2]
            #print (x,y)
            return 1
            break
        else:
            cards[k][0]
            #print("card not match " + str(k))
            k+=1

playerOne = str(input("Please enter player one name: "))
playerTwo = str(input("Please enter player two name: "))
pepperScore = 0
playerScore = 0

while True:
  #peppers turn  
  if pepperScore < 6 and playerScore < 6: #if neither player has won
      resultOne = cardsearch() #run card search on new turned over card 
      if resultOne == 1: #if it returns true (card is found in array)
          #code to point to that specific card 
          pepperScore += 1 #increase peppers score because we know its a match
          print(playerOne,"'s score: ",pepperScore)
      else:
          print("No matches... choosing random card...")
          #randomiser to select different card
          #code to point to that specific card
          if cardsearch() == 1: #check if new random card is a match
              pepperScore += 1 #increase score
          else:
              print("Players turn")

  #players turn
  if pepperScore < 6 and playerScore < 6:
    cardsearch() #read the card the player has turned over
    f = open("pick.txt","r") #open text file of card 
    cardOne = f.read() #read file and store as cardOne
    f.close() #close file
    cardsearch() #read the second card the player has turned over
    f = open("pick.txt","r") #open text file of card
    cardTwo = f.read() #read file and store as cardTwo
    f.close() #close file
    
    if cardOne == cardTwo: #if the players two cards match
        playerScore += 1 #player score increases 
        print(playerTwo,"'s score: ",playerScore)
    else:
        print("No match found by player")


  #elif to catch the game when its finished
  elif pepperScore == 6 or playerScore == 6:
    print("Game over!")
    break

if pepperScore == 6:
  print(playerOne," wins!")
else:
  print(playerTwo," wins!")
 
