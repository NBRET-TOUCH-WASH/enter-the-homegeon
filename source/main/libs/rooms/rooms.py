"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § L-60
            § ADD ACTION(S)

    % FIXME:
        % Target compromised: move in, move in.

        & FIX:
            & Overwatch, target one sterilized.

    µ WHYNOT:
        µ make a floor list with room class instances, use index with movement()?

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ 28/10/2021
            $ 01:54AM
                $ don't really know where im going with this one
"""


#encoding
#coding:utf-8


#libraries/modules



#libs setup


#classes
class Room():#Cabbage fart?
    def __init__(self,number,name,objects,*actions):
        self.number = number
        self.name = name
        self.objects = objects
        self.actions = actions


#functions


#script
F1bedroom = Room(1,"Bedroom",None,"WINDOW: Jump")

F1hallway2 = Room(2,"Beginning of Hallway",None,None)
F1hallway3 = Room(3,"Middle of Hallway",None,None)
F1hallway4 = Room(4,"End of Hallway",None,None)

F1siblingRoom5 = Room(5,"Sibling Room",None,"CLOSET: Change Clothes")
F1parentsRoom6 = Room(6,"Parents Room",None,None)#TODO: ADD ACTION(S)
F1restrooms7 = Room(7,"Restrooms","Pitch-Black Key","TOILET: Flush","TOILET: Use","TOILET: d r i n k  h o l y  b e v e r a g e")

F1hallway8 = Room(8,"Front of the downwards staircase",None,None)



F0downStairs = Room(1,"Bottom of the staircase",None,None)
F0hallway2 = Room(2,"Beginning of the hallway",None,"PAINTING: Observe")
F0hallway3 = Room(3,"End of the hallway",None,None)

F0bathroom = Room(4,"Bathroom","Entrance Key","MIRROR: Look at self","SINK: Wash Hands","SHOWER: Pull Curtain")

F0livingRoom = Room(5,"Living Room",None,None)
F0diningRoom = Room(6,"Dining Room",None,"CHAIR(S): s i t",)

F0entrance = Room(7,"Entrance",None,None)

F0hallway8 = Room(8,"Beginning of the hallway",None,None)
F0hallway9 = Room(9,"End of the hallway",None)
F0basementEntrance = Room(10,"Basement entrance",None,None)