#Author: Anh (Steven) Nguyen
#Created: 09/12/2020
#Last modified: 04/29/2021 by Anh (Steven) Nguyen
import Cube
import Arms2
import time

class CuBot:
    'Cubot Object'
    
    def __init__ (self):        
        #initial cube object created upon initialization of CuBot object (54mm width, 3x3)
        self.cube = Cube.Cube(54, 3)

        #initialize self.arms object with all 3 self.arms (9 servos)
        self.arms = Arms2.AllArms(self.cube)

        self.leftArm = self.arms.leftArm
        self.rightArm = self.arms.rightArm
        self.centerArm = self.arms.centerArm

        #prints the entire dictionary for each arm
        #print(self.leftArm.gripDictionary)
        #print(self.rightArm.gripDictionary)
        #print(self.centerArm.gripDictionary)
        #print(self.leftArm.moveDictionary)
        #print(self.rightArm.moveDictionary)
        #print(self.centerArm.moveDictionary)
        #asdf
    
    def __del__():
        del self.leftArm
        del self.rightArm
        del self.centerArm
        del self.arms
        del self.cube
        
    # This function must be called before operating on a cube, providing its width and order
    def updateCube(self, width, order):
        del self.cube
        self.cube = Cube.Cube(width, order)
        self.arms.updateGripCubeAngle(cube)
        
    # SO (Starting Operation) - takes cube from the user and manipulate it to the correct operating position
    ## Orientation: cube will rotate 90 degrees wrt the Y axis
    def acceptCube(self):
        print("<[^-^]>: Accepting cube ... ", end = '')
        self.centerArm.rotate(-1)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(40, 0) #54mm cube
        #self.centerArm.moveSmooth(self.centerArm.moveDictionary[p - round(cube.width / 2)], 0)
        self.rightArm.moveRelative(90, 0) #54mm cube
        #self.rightArm.moveSmooth(self.rightArm.moveDictionary[maxP - round(cube.width / 2) + c], 0) #c is constant in mm that will take maxP to floor
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripReleaseAngle)
        time.sleep(0.5)
        self.rightArm.moveSmooth(self.rightArm.moveMinAngle, 0.01)
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.rotate(0)
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        time.sleep(0.1)
        self.centerArm.moveRelative(-10, 0)
        self.rightArm.moveSmooth(self.rightArm.moveInitAngle, 0.01)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripInitAngle)
        time.sleep(0.5)
        self.centerArm.moveSmooth(self.centerArm.moveInitAngle, 0.02)
        time.sleep(0.5)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(0.5)
        print("[COMPLETE]")

    # CO (Consistency Operation) - brings the cube to the correct operating height
    ## Orientation: no change
    def checkHeight(self):
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(-20, 0.01)
        self.rightArm.rotate(1)
        time.sleep(0.5)
        self.centerArm.moveRelative(50, 0.01)
        time.sleep(0.1)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        self.centerArm.moveRelative(-50, 0.01)
        self.rightArm.rotate(0)
        time.sleep(0.5)
        self.centerArm.moveRelative(20, 0.01)
        time.sleep(0.1)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1)
        
    # EO (Ending Operation) - brings cube back to the starting starting position
    ## Orientation: cube will rotate -90 degrees wrt the Y axis
    def presentCube(self):
        print("<[^-^]>: Presenting cube ... ", end = '')
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        time.sleep(0.5)
        self.rightArm.move(self.rightArm.moveMinAngle)
        self.centerArm.move(self.centerArm.moveInitAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(40, 0.02)
        self.centerArm.rotate(-1)
        time.sleep(0.5)
        self.rightArm.move(self.rightArm.moveInitAngle)
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1.5)
        self.centerArm.grip(self.centerArm.gripInitAngle)
        time.sleep(0.5)
        self.rightArm.moveRelative(90, 0.02)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripInitAngle)
        time.sleep(0.5)
        self.rightArm.move(self.rightArm.moveInitAngle)
        self.centerArm.move(self.centerArm.moveInitAngle)
        time.sleep(0.5)
        self.centerArm.rotate(0)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        print("[COMPLETE]")

    # PO (Primary Operation) - rotate left layer 90 degrees (1) or -90 degrees (-1)
    ## Orientation: no change
    def L(self, numLayers, direction):
        print("<[^-^]>: Manipulating left face ... ", end = '')
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(23, 0.02)
        self.leftArm.moveRelative(20, 0.02)
        time.sleep(0.11)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1.5)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        time.sleep(0.5)
        self.leftArm.rotate(direction)
        time.sleep(0.5)
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(40, 0.02)
        time.sleep(0.1)
        self.leftArm.rotate(0)
        self.leftArm.move(self.leftArm.moveInitAngle)
        self.centerArm.moveSmooth(self.centerArm.moveInitAngle, 0.02)
        time.sleep(0.1)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1)
        print("[COMPLETE]")
        
    # PO (Primary Operation) - rotate right layer 90 degrees (1) or -90 degrees (-1)
    ## Orientation: no change
    def R(self, numLayers, direction):
        print("<[^-^]>: Manipulating right face ... ", end = '')
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        self.leftArm.grip(self.leftArm.gripMaxAngle)    
        time.sleep(0.5)
        self.centerArm.moveRelative(-20, 0.02)
        self.rightArm.moveRelative(20, 0.02)
        time.sleep(0.11)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        time.sleep(0.5)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1.5)
        self.rightArm.rotate(direction)
        time.sleep(0.5)
        self.rightArm.gripRelative(80, 0)
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(-40, 0.02)
        time.sleep(0.1)
        self.rightArm.rotate(0)
        self.rightArm.move(self.rightArm.moveInitAngle)
        self.centerArm.moveSmooth(self.centerArm.moveInitAngle, 0.02)
        time.sleep(0.1)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        time.sleep(1)
        print("[COMPLETE]")

    # PO (Primary Operation) - rotate cube 90 degrees (1) or -90 degrees (-1)
    ## Orientation: cube will rotate 90 degrees (1) or -90 degrees (-1) wrt the Y axis
    def Y(self, direction):
        print("<[^-^]>: Rotating cube ... ", end = '')
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        time.sleep(0.5)
        self.arms.moveSideArms(-50, 0.01)
        self.centerArm.rotate(-direction)
        time.sleep(0.5)
        self.arms.moveSideArms(50, 0.01)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(1)
        self.rightArm.grip(self.rightArm.gripMaxAngle)
        self.leftArm.grip(self.leftArm.gripMaxAngle)
        time.sleep(0.5)
        self.arms.moveSideArms(-50, 0)
        self.centerArm.rotate(0)
        self.centerArm.moveRelative(15 * -direction, 0)
        time.sleep(0.5)
        self.arms.moveSideArms(50, 0)
        self.rightArm.grip(self.rightArm.gripCubeAngle)
        self.leftArm.grip(self.leftArm.gripCubeAngle)
        time.sleep(1)
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        time.sleep(0.5)
        self.centerArm.moveRelative(30 * direction, 0)
        time.sleep(0.5)
        self.centerArm.move(self.centerArm.moveInitAngle)
        time.sleep(0.5)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(1)
        print("[COMPLETE]")
        
    # PO (Primary Operation) - rotate Down layer 90 degrees (1) or -90 degrees (-1)
    ## Orientation: no change
    def D(self, numLayers, direction):
        print("<[^-^]>: Manipulating bottom face ... ", end = '')
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        time.sleep(0.5)
        self.arms.moveSideArms(-25, 0.01)
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(1)
        self.centerArm.rotate(direction)
        time.sleep(1)
        self.centerArm.grip(self.centerArm.gripMaxAngle)
        self.arms.moveSideArms(-20, 0.01)
        self.centerArm.rotate(0)
        time.sleep(0.5)
        self.arms.moveSideArms(45, 0.01)
        
        self.centerArm.grip(self.centerArm.gripCubeAngle)
        time.sleep(1)
        print("[COMPLETE]")
        
# # PO (Primary Operation) - rotate Up layer 90 degrees (1) or -90 degrees (-1)
# ## Orientation: cube will rotate -90 degrees (1) or 90 degrees (-1) wrt the Y axis
# def U(layers, direction):
#     #yet to be implemented
#     time.sleep(1)

############## Begin Testing ##############
print("testing blah blah blah")
#self.centerArm.move(self.centerArm.moveMaxAngle)
#time.sleep(1)
#self.leftArm.gripTest()
#self.leftArm.grip3by3Test()
#self.leftArm.rotateTest(1)
#self.leftArm.moveTest(1)
#self.leftArm.test()
#self.centerArm.move(self.centerArm.moveInitAngle)

#self.centerArm.move(self.centerArm.moveMinAngle)
#time.sleep(1)
#self.rightArm.gripTest()
#self.rightArm.grip3by3Test()
#self.rightArm.rotateTest(1)
#self.rightArm.moveTest(1)
#self.rightArm.test()
#self.centerArm.move(self.centerArm.moveInitAngle)

#time.sleep(1)
#self.centerArm.rotate(1)
#time.sleep(2)
#self.centerArm.gripTest()
#self.centerArm.grip3by3Test()
#self.centerArm.rotateTest(1)
#self.centerArm.moveTest(1)
#self.centerArm.test()
    
#acceptCube()
#L(1)
#R(1)
#Y(1)
#L(1)
#R(1)
#Y(1)
#Y(1)
#L(-1)
#R(-1)
#Y(1)
#L(-1)
#R(-1)

#L(1)
#B(1)
#R(1)

#checkHeight()

#presentCube()
    
#self.leftArm.grip(self.leftArm.gripMinAngle)
#time.sleep(5)
#self.leftArm.grip(self.leftArm.gripMaxAngle)
#time.sleep(5)
    
#self.rightArm.grip(self.rightArm.gripCubeAngle)
#time.sleep(5)
#self.rightArm.grip(self.rightArm.gripInitAngle)
#print(self.rightArm.gripCubeAngle)


############# Begin Execution ##############


########### Garbage Collection #############
