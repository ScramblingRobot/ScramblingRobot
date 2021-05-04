import math
#from CuBot2 import L, R, D, Y
from CuBot2 import CuBot
# The below functions were used in testing without connecting to the actual robot
# def L(self, layers, degree):
#     pass

# def R(self, layers, degree):
#     pass

# def D(self, layers, degree):
#     pass

# def Y(self, degree):
#     pass

class Face(object): # Since python doens have Enum, made my own as it makes tracking code cleaner/simpiler
    cuBot   = CuBot(54, 3)
    Front   = "F"
    Left    = cuBot.L
    Back    = "B"
    Right   = cuBot.R
    Up      = "U" #Up no Longer Exist, but keep in for coherency
    Down    = cuBot.D
Face = Face()   # Enum to signify face of Cube

class Dir(object):
    South   = 0
    West    = 1
    North   = 2
    East    = 3
    Above   = 4
    Below   = 5
Dir = Dir()


# May not be needed 
Dimension = 3   
Boundary = math.floor(Dimension/2)

F = ["Front","Left","Back","Right","Up","Down"] # IGNORE For internal test use (displaying Sequences)


class Sequence(object):
    Face = None
    Width = 1
    Degree = 1
    def __init__(self,input):   # Translate text into scramble class Sequence
        for char in input:     
            if char == 'y':     # No need to set degree since by defualt its 1
                self.Face = Face.cuBot.Y
            if char == 'F':
                self.Face = Face.Front
            elif char == 'L':
                self.Face = Face.Left
            elif char == 'B':
                self.Face = Face.Back
            elif char == 'R':
                self.Face = Face.Right
            elif char == 'U':
                self.Face = Face.Up
            elif char == 'D':
                self.Face = Face.Down
            elif char == 'w':                       # IMPORTANT:  xDw -> x + 1-layer D turn. 2Dw means 2 layers, etc
                self.Width = int( input[0] )      # IGNORE ( float( input[0] ) if input[0].isdigit()  else 1)
            elif char == '2':   
                self.Degree = 2
            elif char == "'":
                self.Degree = -1

def perform(input):
    for s in input.split(): 
        sequence = Sequence(s)

        if sequence.Face == Face.cuBot.Y:
            if sequence.Degree == 2:
                Face.cuBot.Y(1)
                Face.cuBot.Y(1)                
            else:
                Face.cuBot.Y(sequence.Degree)
            print("Rotate Entire Cube: {0} degrees (Using Bottom Arm)\n".format(sequence.Degree*90))
        else:
            width = sequence.Width
            if sequence.Degree == 2:
                sequence.Face(width, 1)
                sequence.Face(width, 1)
            else:
                sequence.Face(sequence.Width, sequence.Degree)
            print("Rotate {0} Face: {1} Layers {2} Degrees\n".format(sequence.Face.__name__, sequence.Width, sequence.Degree*90))
        # elif sequence.Face == Face.Down:
        #     print("Rotate Bottom Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree*90))
        # else:
        #     if sequence.Face == Face.Left:
        #         print("Rotate Left Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree*90))
        #     else:
        #         print("Rotate Right Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree*90))
