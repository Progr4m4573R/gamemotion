
import os# built in module
import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"
import SpawnPepperTestPointing as SP

from past.builtins.misc import execfile
folder_directory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
os.chdir(folder_directory)

#card_found = CS.found#imported GLOBAL Boolean
#Pepper_Turn = True ##local boolean
#Player_Turn = False
#GameOver = CS.Game_Over

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
   
#Pepper Points at a random card#                                    ***needs work***
'''
if  CS.found == False & Pepper_Turn == True:#will need to make this a button press
    StartRobotMotion()
    SP.Random_Point()
    CS.GameScore()# Always gets checked
    Pepper_Turn = False
    Player_Turn = True
#Pepper points at a matching card
if CS.found == True & Pepper_Turn == True:#
    StartRobotMotion()
    SP.Point_at_Match()
    CS.GameScore()
    Pepper_Turn = False
else:
    print("Searching for match...")
'''

StartOpenCv()#Start OpenCv
StartRobotMotion()#Start pepper simulation
StartCardScanner()#Start card scanner code
MainDirectory()#changes directory back so we don't get text file not found exception


print('This is the location we are in: '+os.getcwd())#shows the directory we are in
print('These are the files in the location: ')
print(os.listdir())##shows what files are in the location
#SP.Random_Point()# This doesn't work becaude random point is an embedded method so we need a different way to acces it outside of the code, right now it runs fine within the code