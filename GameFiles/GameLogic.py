import os# built in module
import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"
import SpawnPepperTestPointing as SP
import random
from past.builtins.misc import execfile

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

Pepper_Turn = False 
Player_Turn = False
player_name = ''

pepperScore = 0
playerScore = 0

OpenCvDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/DummyOpenCVCode/Debug/'#location of .exe file
OpenCvFileName = 'DummyOpenCVCode'#name of your .exe file

RobotMotionName = 'SpawnPepperTestPointing.py'

#Functions for starting different processes
def StartOpenCv():#should only be called once
    try:
        os.chdir(OpenCvDirectory)
        os.startfile(OpenCvFileName)
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

def NewCardGenerator():#i have had to use this for the purpose of a demo because i cannot get the open cv code running, it serves a smiliar purpose
    Colour1 = "BLACK "
    Colour2 = "RED "

    for x in range (2):
        cardnumber1 = random.randint(1,5)
        cardnumber2 = random.randint(1,5)
        cardnumber3 = random.randint(1,5)
    for i in range (2):
        cardcolour = random.randint(1,2)
        if cardcolour == 1:
            card = Colour1 + str(cardnumber1)+","+str(cardnumber2)+","+str(cardnumber3)
            return card
        if cardcolour == 2:
            card = Colour2 + str(cardnumber1)+","+str(cardnumber2)+","+str(cardnumber3)
            return card
StartOpenCv()#Start OpenCv
StartRobotMotion()#Start pepper simulation
SP.StartUp()
MainDirectory()#changes directory back so we don't get text file not found exception

player_name = str(input("Please input your name: "))
while True:
    if pepperScore < 6 and playerScore < 6: #if neither player has won
        try:
            print("\npress 1 if it is your turn\npress 2 if it is pepper's go ")
            first_player = input()# gets what the user types in

            if first_player == '1':

                Player_Turn = True
                Pepper_Turn = False
                
                print("Player's go")	

            elif first_player == '2':
                Pepper_Turn = True
                Player_Turn = False
                print("Pepper's go")            
            result = CS.cardsearch()   
        #peppers turn  
            if  Pepper_Turn == True: #if it returns true (card is found in array) 
                #print("Pepper's turn")  
        
                if result[0] == "match found":           
                    #code to point to that specific card 
                    pepperScore += 1 #increase peppers score because we know its a match
                    print("Pepper's score: ",pepperScore)
                    SP.Point_at_Match()#Pepper points at a matching card
                    CS.cardsearch()
                    print("Pointing at match...")
                    Pepper_Turn = False                

                #player's turn
            if Player_Turn == True:  
                #print("player turn")
                player_match = str(input("Did you get a match? Y or N"))          
                if player_match == "Y": #if the players two cards match
                    playerScore += 1 #player score increases 
                    print(player_name,"'s score: ",playerScore)
                    Player_Turn = False
                else:
                    print("No match found by player")
                    Player_Turn = False

        except Exception as e:   
            #elif to catch the game when its finished
            if pepperScore == 6:
                print("Game over!")
                print("Pepper wins!")
                break
            elif playerScore == 6:
                print("Game over!")
                print(player_name," wins!")
                break            
            print("No matches found")
            SP.Random_Point()#point at random card
            CS.cardsearch()
            Pepper_Turn = False

            with open('pick.txt', 'w') as pickFile:
                pickFile.write(str(NewCardGenerator()))
            continue
        except TypeError as e:
            print (e)
