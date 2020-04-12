import os# built in module
import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"
import SpawnPepperTestPointing as SP

from past.builtins.misc import execfile
folder_directory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
os.chdir(folder_directory)

OpenCvDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/DummyOpenCVCode/Debug/'#location of .exe file
OpenCvFileName = 'DummyOpenCVCode'#name of your .exe file
CardScannerDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
CardScannerName = 'CardScanner.exe'
RobotMotionDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
RobotMotionName = 'SpawnPepperTestPointing.exe'

#Functions for starting different processes
def StartOpenCv():#should only be called once
    try:
        os.chdir(OpenCvDirectory)
        os.startfile(OpenCvFileName)
    except Exception as e:
            print(e)

def StartCardScanner():## is only run once each time it is called
    try:
        os.chdir(CardScannerDirectory)
        os.startfile(CardScannerName)
    except Exception as e:
            print(e)
    
def StartRobotMotion():#should only be called once
    try:
        os.chdir(RobotMotionDirectory)
        execfile('SpawnPepperTestPointing.py')# the start file command doesn't work for this so had to use execfile
    except Exception as e:
            print(e)

def MainDirectory():
    os.chdir(folder_directory)


StartOpenCv()#Start OpenCv
StartRobotMotion()#Start pepper simulation
StartCardScanner()#Start card scanner code
MainDirectory()#changes directory back so we don't get text file not found exception


#-------------------------------------------------------------------------------#


pepperScore = 0
playerScore = 0

while True: #infinite loop to simulate game
    #pepper goes first
    if pepperScore < 6 and playerScore < 6: #if neither player has reached score limit
        if CS.cardsearch() == 1: #if cardSearch returns 1, meaning a match has been found
            StartRobotMotion()
            SP.Point_at_match() #point at the matching card 
            pepperScore += 1 #increase score by 1

        elif CS.cardsearch() == 0: #if theres no match found
            StartRobotMotion()
            SP.Random_Point() #point at random card

            #Need some code here to check whether random card matches previous card

        else:
            print("Players turn")

    #players turn
    if pepperScore < 6 and playerScore < 6:
        CS.cardsearch() #call cardsearch to store card for pepper
        #need to store the card that was read
        CS.cardsearch() #call again to see whether player gets a match
        #code to compare the two cards
        #if cards match, playerScore++, else pepperTurn

    elif pepperScore == 6 or playerScore == 6:
        print("Game over")
        print("Pepper: "+str(pepperScore)+" Player: "+str(playerScore))


        
    
    



