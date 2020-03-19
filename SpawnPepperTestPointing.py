print("Imported SpawnPepperTesting")
import cv2
from qibullet import SimulationManager
from qibullet import PepperVirtual
import time
import random
import CardScanner as CS # abreviates the name so it is easier to use . can also try "FROM CardScanner import cardsearch,x,y because x and y are global variables"

card_x = CS.x
card_y = CS.y

for x in range(2):# creates two random variables to get pepper to point at a random location
 random_x =  random.randint(0,5)#gridwidth
 random_y = random.randint(0,4)#gridheight

#Pointing
def Point_at_Match():  
    pepper.setAngles("RShoulderRoll", ((2.2/10)*card_x), 0.1)## rolls shoulder in x direction should, come after movement in y direction 
    time.sleep(3.0)
    ## pepper.setAngles("RShoulderRoll", 0.0, 0.1)
    pepper.setAngles("RShoulderPitch", ((2.2/10)*card_y), 0.1)
    time.sleep(3.0)

def Random_Point():
    pepper.setAngles("RShoulderRoll", ((2.2/10)*random_x), 0.1)## rolls shoulder in x direction should, come after movement in y direction 
    time.sleep(3.0)
    ## pepper.setAngles("RShoulderRoll", 0.0, 0.1)
    pepper.setAngles("RShoulderPitch", ((2.2/10)*random_y), 0.1)
    time.sleep(3.0)

def StartUp():
    	#ARMS STRETCHED FRONT
    pepper.goToPosture("StandZero", 0.6) ##or StandInit // always start with this
    time.sleep(2.0)
    
    ##Getting ready to point stance
    pepper.setAngles("RShoulderPitch", 0.4, 0.1)## moves in y direction
    time.sleep(1.0)
    pepper.setAngles("RElbowYaw", 1.5, 0.1)## Rotates elbow 
    time.sleep(1.0)
    ##ReadyPosition
    pepper.setAngles(["RElbowRoll", "RShoulderPitch"], [1.5, 1.7],  [0.1, 0.1])
    ## at this point we caucluate the card we need to point at and then its position then begin to point at it.
    time.sleep(3.0)

def Reset():
    ##Reset
    pepper.setAngles(["RElbowRoll", "RShoulderPitch"], [0.0, 0.6],  [0.1, 0.1])
    pepper.setAngles("RElbowYaw", 0.8, 0.1)
    time.sleep(3.0)

if __name__ == "__main__":
    simulation_manager = SimulationManager()
    client_id = simulation_manager.launchSimulation(gui=True)
 	#Spawn PEPPER
    pepper = simulation_manager.spawnPepper(
        client_id, spawn_ground_plane=True)
	
  


'''
    # Add other objects to the simulation...
    while True:
        # Retrieving and displaying the synthetic image using OpenCV
        img = pepper.getCameraFrame()
        cv2.imshow("synthetic top camera", img)
        cv2.waitKey(1)

        resolution = pepper.getCameraResolution()#GETS camera resolution
        time.sleep(1.0)
        print('width : ' +str(resolution.width))
        time.sleep(1.0)
        print('height : ' +str(resolution.height))
       ''' 
        #pepper.unsubscribeCamera(PepperVirtual.ID_CAMERA_TOP)
