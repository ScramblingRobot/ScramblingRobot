import math

class Face(object): # Since python doens have Enum, made my own as it makes tracking code simpiler
    Front   = 0
    Left    = 1
    Back    = 2
    Right   = 3
    Up      = 4
    Down    = 5
Face = Face()   # Enum to signify face of Cube

class Dir(object):
    South   = 0
    West    = 1
    North   = 2
    East    = 3
    Above   = 4
    Below   = 5
Dir = Dir()

GridUnit = 1.0

Dimension = 3
Boundary = math.floor(Dimension/2)
