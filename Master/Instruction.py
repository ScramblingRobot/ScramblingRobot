from Global import *

class Instruction(object):
    Face    = None
    Cord    = 0
    Degree  = 90
    def out(self): # [Temporary] used to output Instruction 
        print("Face: {0}\nCord: {1}\nDegree: {2}\n".format( f[self.Face], self.Cord, self.Degree))

# Translate text into class Instruction 
def translate(input):
    instruction = Instruction()
    for char in input:
        if char == 'F':
            instruction.Face = Face.Front
        elif char == 'L':
            instruction.Face = Face.Left
        elif char == 'B':
            instruction.Face = Face.Back
        elif char == 'R':
            instruction.Face = Face.Right
        elif char == 'U':
            instruction.Face = Face.Up
        elif char == 'D':
            instruction.Face = Face.Down
        elif char == 'W':
            instruction.Cord = GridUnit * ( float( input[0] ) if input[0].isdigit()  else 2)
        elif char == '2':
            instruction.Degree = 180
        elif char == "'":
            instruction.Degree = -90
    return instruction