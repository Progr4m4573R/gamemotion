import os# built in module
import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"
import SpawnPepperTestPointing as SP
from past.builtins.misc import execfile

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

#card_found = CS.found#imported GLOBAL Boolean
Pepper_Turn = False 
Player_Turn = False
player_name = ''

pepperScore = 0
playerScore = 0

OpenCvDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/DummyOpenCVCode/Debug/'#location of .exe file
OpenCvFileName = 'DummyOpenCVCode'#name of your .exe file

CardScannerName = 'CardScanner.exe'

RobotMotionName = 'SpawnPepperTestPointing.py'

#Functions for starting different processes
def StartOpenCv():#should only be called once
    try:
        os.chdir(OpenCvDirectory)
        os.startfile(OpenCvFileName)
    except Exception as e:
            print(e)

def StartCardScanner():## is only run once each time it is called
    try:
        os.chdir(folder_directory)
        os.startfile(CardScannerName)
    except Exception as e:
            print(e)
    
def StartRobotMotion():#should only be called once
    try:
        os.chdir(folder_directory)
        execfile(RobotMotionName)# the start file command doesn't work for this so had to use execfile
    except Exception as e:
            print(e)

def MainDirectory():
    os.chdir(folder_directory)
   
    print('\nThis is the location we are in: '+os.getcwd())#shows the directory we are in
    print('These are the files in the location: ')
    print(os.listdir())##shows what files are in the location

StartOpenCv()#Start OpenCv
StartCardScanner()#Start card scanner code
StartRobotMotion()#Start pepper simulation

MainDirectory()#changes directory back so we don't get text file not found exception

print("\npress 1 to go first\npress 2 to let pepper go first")
first_player = input()# gets what the user types in

if first_player == '1':
    player_name = str(input("Please input your name: "))
    Player_Turn = True
    Pepper_Turn = False
    
    print("The player choose to go first")	

elif first_player == '2':
    Pepper_Turn = True
    Player_Turn = False
    print("Pepper is going first")

while True:
#peppers turn  
    if pepperScore < 6 and playerScore < 6: #if neither player has won

        if  Pepper_Turn == True: #if it returns true (card is found in array) 
            print("Pepper's turn")         
            if CS.cardsearch() == "match found":           
                #code to point to that specific card 
                pepperScore += 1 #increase peppers score because we know its a match
                print("Pepper's score: ",pepperScore)
                SP.Point_at_Match()#Pepper points at a matching card
                Pepper_Turn = False
                Player_Turn = True
                print("Pointing at match...")
                                        

            elif  CS.cardsearch == "match not found": 
                print("Pepper is pointing at a random card")
                SP.Random_Point()#point at random card
                CS.cardsearch()
                CS.GameScore()# check the score
                Pepper_Turn = False
                Player_Turn = True
            #player's turn
        if Player_Turn == True:  
            print("player turn")          
            if CS.cardsearch()=="match found": #if the players two cards match
                playerScore += 1 #player score increases 
                print(player_name,"'s score: ",playerScore)
                Player_Turn = False
                Pepper_Turn = True
            else:
                print("No match found by player")
                Player_Turn = False
                

        #elif to catch the game when its finished
        if pepperScore == 6:
            print("Game over!")
            print("Pepper wins!")
            break
        elif playerScore == 6:
            print("Game over!")
            print(player_name," wins!")
            break
        else:
            print ("logic error, No condition was met")
           #bremoved a break here
