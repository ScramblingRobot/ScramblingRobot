from Global import *

class Sequence(object):
    Face = None
    Width = 0
    Degree = 90
    def Out(self): # [Temporary] used to output Instruction 
        print("Face: {0}\nCord: {1}\nDegree: {2}\n".format( f[self.Face], self.Cord, self.Degree))

# Translate text into scramble class Sequence 
def translate(input):
    sequence = Sequence()
    for char in input:
        if char == 'F':
            sequence.Face = Face.Front
        elif char == 'L':
            sequence.Face = Face.Left
        elif char == 'B':
            sequence.Face = Face.Back
        elif char == 'R':
            sequence.Face = Face.Right
        elif char == 'U':
            sequence.Face = Face.Up
        elif char == 'D':
            sequence.Face = Face.Down
        elif char == 'W':   # Maybe in default put an if to see if its an int and if so then use that for how many layers W it is
            sequence.Width = ( float( input[0] ) if input[0].isdigit()  else 2)
        elif char == '2':   
            sequence.Degree = 180
        elif char == "'":
            sequence.Degree = -90
    return sequence
