class Face(object): # Since python doens have Enum, made my own as it makes tracking code simpiler
    Front   = 0
    Left    = 1
    Back    = 2
    Right   = 3
    Up      = 4
    Down    = 5
Face = Face()

class Dir(object):
    South   = 0
    West    = 1
    North   = 2
    East    = 3
    Above   = 4
    Below   = 5
Dir = Dir()

Arms = {    # Will change to dictionary of Arm Objects, with key as direction of arm relative to cube
        Dir.West    : "Rotate West Arm!",
        Dir.East    : "Rotate East Arm!",
        Dir.Below   : "Rotate Below Arm!"
       }

GridUnit = 1.0

# [Temporary] used for output tracked instead of seein index, display names
f = ["Front", "Left", "Back", "Right", "Up", "Down"]
d = ["South", "West", "North", "East", "Above", "Below"]