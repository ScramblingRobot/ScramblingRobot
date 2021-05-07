from CuBot2 import CuBot
import time

cuBot = CuBot()
cuBot.updateCube(61, 4)

def testAcceptCube():
    cuBot.acceptCube()
    
def testPresentCube():
    cuBot.presentCube()

def testCheckHeight():
    cuBot.checkHeight()

def testL(numLayers, direction):
    cuBot.L(numLayers, direction)
    
def testR(numLayers, direction):
    cuBot.R(numLayers, direction)

def testD(numLayers, direction):
    cuBot.D(numLayers, direction)

def testY(numlayers, direction):
    cuBot.Y(direction)
    
def testGrip(arm, position, waitTime):
    if position == "max":
        arm.grip(arm.gripMaxAngle)
    elif position == "min":
        arm.grip(arm.gripMinAngle)
    else:
        arm.grip(arm.gripDictionary[position])
    time.sleep(waitTime)

def testMove(arm, position, waitTime):
    if position == "max":
        arm.moveSmooth(arm.moveMaxAngle, 0.01)
    elif position == "min":
        arm.moveSmooth(arm.moveMinAngle, 0.01)
    else:
        arm.moveSmooth(arm.moveDictionary[position], 0.01)
    time.sleep(waitTime)
    
def unitTestAcceptCube(moveNumber):
    if moveNumber == 1:
        cubeWidth = 54
        targetPosition = 85
        
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth])
        time.sleep(1)
        cuBot.centerArm.rotate(-1)
        time.sleep(1)
        testMove(cuBot.centerArm, targetPosition - round(cubeWidth / 2), 2)
        time.sleep(2)
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth + 15])
        time.sleep(2)
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth])
        time.sleep(1)
        cuBot.centerArm.rotate(0)
        time.sleep(1)
        cuBot.centerArm.grip(cuBot.centerArm.gripInitAngle)
    
    elif moveNumber == 2:
        cubeWidth = 54
        c = 25

        testMove(cuBot.centerArm, 15, 1)
        testMove(cuBot.rightArm, 93 - round(cubeWidth / 2) + c, 2)
        testMove(cuBot.rightArm, 46, 1)
        testMove(cuBot.centerArm, 31, 1)
        
######### Begin Testing ##########
#testAcceptCube()
#testPresentCube()
#testCheckHeight()
#testL(2, -1)
#testR(1, 1)
#testD(1, 1)
#testY(1, 1)
#testGrip(cuBot.centerArm, 79, 5)
#testMove(cuBot.rightArm, 46, 1)
#unitTestAcceptCube(1)
#unitTestAcceptCube(2)

############## Finished ###############
# gripDictionary calibration for all 3 arms
# moveDictionary calibration for center and right arm
# primary operating-function acceptCube() calibration to support variability in cube width and order

del cuBot
