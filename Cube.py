#Author: Anh (Steven) Nguyen
#Created: 04/18/2021
#Last modified: 04/29/2021 by Anh (Steven) Nguyen

class Cube:
    'Cube object'
    # width: width of the cube in mm
    # order: number of layers the cube has
    # state: current state of the cube
    
    def __init__(self, width, order):
        self.width = width
        self.order = order
        self.state = [[[0 for column in range(order)] for row in range(order)] for side in range(6)]
        print ("CREATED: %dmm %dx%d Rubiks Cube" % (self.width, self.order, self.order))
        
    def __del__(self):
        print ("DELETED: %dmm %dx%d Rubiks Cube" % (self.width, self.order, self.order))
    
    def solvedState(self):
        for side in range (6):
            for row in range (self.order):
                for column in range (self.order):
                    self.state[side][row][column] = side
    
    def printCube(self):
        for side in range (6):
            print("Side %d:" % (side))
            for row in range (self.order):
                if row == 0:
                    print("[", end = '')
                else:
                    print(" ]\n[", end = '')
                for column in range (self.order):
                    print("%2d" % (self.state[side][row][column]), end = '')
                    if row == self.order - 1 & column == self.order - 1:
                        print(" ]")