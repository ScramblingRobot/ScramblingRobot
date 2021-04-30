from Global import *

class Sequence(object):
    Face = None
    Width = 0
    Degree = 90
    def __init__(self,input):   # Translate text into scramble class Sequence
        for char in input:     
            if char == 'y':     # No need to set degree since by defualt its 90
                self.Face = 'y'
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
            elif char == 'W':                       # IMPORTANT:  xDw -> x-layer D turn. 0 meants 1, etc
                self.Width = float( input[0] )      # IGNORE ( float( input[0] ) if input[0].isdigit()  else 1)
            elif char == '2':   
                self.Degree = 180
            elif char == "'":
                self.Degree = -90

def perform(input):
    for s in input.split(): 
        sequence = Sequence(s)

        if sequence.Face == 'y':    
            print("Rotate Entire Cube: {0} degrees (Using Bottom Arm)\n".format(sequence.Degree))
        elif sequence.Face == Face.Down:
            print("Rotate Bottom Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree))
        else:
            if sequence.Face == Face.Left:
                print("Rotate Left Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree))
            else:
                print("Rotate Right Arm: Layer {0} and {1} degrees\n".format(sequence.Width,sequence.Degree))
