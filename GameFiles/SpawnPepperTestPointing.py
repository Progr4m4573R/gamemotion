print("Imported SpawnPepperTesting")
import cv2
from qibullet import SimulationManager
from qibullet import PepperVirtual
import time
import random
from CardScanner import cardsearch # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"

Robot  = "pepper"


for x in range(2):# creates two random variables to get pepper to point at a random location
 random_x =  random.randint(-3,5)#gridwidth max 5
 random_y = random.randint(0,4)#gridheight  max 4


#if __name__ == "__main__":
simulation_manager = SimulationManager()
client_id = simulation_manager.launchSimulation(gui=True)
#Spawn PEPPER
Robot = simulation_manager.spawnPepper(
    client_id, spawn_ground_plane=True)

#Pointing
def Point_at_Match():  
    Reset()
    Robot.setAngles("RShoulderRoll", (-1*(2.2/20)*int(cardsearch()[1])), 0.1)## rolls shoulder in x direction should, come after movement in y direction 
    time.sleep(3.0)
    ## pepper.setAngles("RShoulderRoll", 0.0, 0.1)
    Robot.setAngles("RShoulderPitch", ((2.2/20)*int(cardsearch()[2])), 0.1)
    time.sleep(3.0)

def Random_Point():
    Reset()
    Robot.setAngles("RShoulderRoll", ((2.2/10)*random_x), 0.1)## rolls shoulder in x direction should, come after movement in y direction 
    time.sleep(3.0)
    ## pepper.setAngles("RShoulderRoll", 0.0, 0.1)
    Robot.setAngles("RShoulderPitch", ((2.2/10)*random_y), 0.1)
    time.sleep(3.0)

def StartUp():
    #ARMS STRETCHED FRONT
    Robot.goToPosture("StandZero", 0.6) ##or StandInit // always start with this
    time.sleep(2.0)
    
    ##Getting ready to point stance
    Robot.setAngles("RShoulderPitch", 0.4, 0.1)## moves in y direction
    time.sleep(1.0)
    Robot.setAngles("RElbowYaw", 1.5, 0.1)## Rotates elbow 
    time.sleep(1.0)
    ##ReadyPosition
    Robot.setAngles(["RElbowRoll", "RShoulderPitch"], [1.5, 1.7],  [0.1, 0.1])
    ## at this point we caucluate the card we need to point at and then its position then begin to point at it.
    time.sleep(3.0)

def Reset():
    ##Reset
    Robot.setAngles(["RElbowRoll", "RShoulderPitch"], [0.0, 0.6],  [0.1, 0.1])
    Robot.setAngles("RElbowYaw", 0.8, 0.1)
    time.sleep(3.0)


print(random_x, random_y)#****uncomment to shows the x and y location Pepper is currently pointing at***
# code executes instantly if this isn't added

'''
Robot.subscribeCamera(PepperVirtual.ID_CAMERA_TOP)
print("Activating Camera...")##would instantly close if this wasn't added


# Add other objects to the simulation...
while True:
    # Retrieving and displaying the synthetic image using OpenCV
    img = Robot.getCameraFrame()
    cv2.imshow("synthetic top camera", img)
    cv2.waitKey(1)
    False
    #resolution = Robot.getCameraResolution()#GETS camera resolution
    # time.sleep(1.0)
    # print('width : ' +str(resolution.width))
    # time.sleep(1.0)
    #print('height : ' +str(resolution.height))
    
'''
