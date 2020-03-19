import os# built in module

import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"
import SpawnPepperTestPointing as SP

card_found = CS.found#imported GLOBAL Boolean
Pepper_Turn = True ##local boolean

OpenCvDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/DummyOpenCVCode/Debug/'#location of .exe file
OpenCvFileName = 'DummyOpenCVCode'#name of your .exe file
CardScannerDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
CardScannerName = 'CardScanner.exe'
RobotMotionDirectory = 'C:/Users/Ghost/OneDrive - University of Lincoln/Year 2 second half/TSE Group Project/Project work/gamemotion/'
RobotMotionName = 'SpawnPepperTestPointing.exe'
RandomPointing = SP.Random_Point()#calls the random pointing function from SpawnPepper


def StartOpenCv():
    try:
        os.chdir(OpenCvDirectory)
        os.startfile(OpenCvFileName)
    except Exception as e:
            print(e)


def StartCardScanner():
    try:
        os.chdir(CardScannerDirectory)
        os.startfile(CardScannerName)
    except Exception as e:
            print(e)

def StartRobotMotion():
    try:
        os.chdir(RobotMotionDirectory)
        os.startfile(RobotMotionName)
    except Exception as e:
            print(e)


def GameStatus():# needs to look at the score and decide who has won
    
StartOpenCv()
StartCardScanner()

#Run pepper Ready Stance code
SP.StartUp()

#Pepper Points at a random card
if Pepper_Turn == True:#will need to make this a button press
    StartRobotMotion()
    SP.Random_Point()
    Pepper_Turn = False
#Pepper points at a matching card
if CS.found == True & Pepper_Turn == True:#
    StartRobotMotion()
    SP.Point_at_Match()
    Pepper_Turn = False
else:
    print("Searching for match...")


print(os.getcwd())#shows the directory we are in
print(os.listdir())##shows what files are in the location
