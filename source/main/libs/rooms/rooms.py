"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § Amplify weapons on Wallhammer.

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
#all objects currently set to None for safety, as idk what i want to add to rooms yet
F1bedroom = Room(1,"Bedroom",None,"Window: Jump")

F1hallway2 = Room(2,"Beginning of Hallway",None)
F1hallway3 = Room(3,"Middle of Hallway",None)
F1hallway4 = Room(4,"End of Hallway",None)

F1siblingRoom5 = Room(5,"Sibling Room",None)
F1parentsRoom6 = Room(6,"Parents Room",None)
F1restrooms7 = Room(7,"Restrooms",None)

F1hallway8 = Room(8,"Front of the downwards staircase",None)



F0downStairs = Room(1,"Bottom of the staircase",None)
F0hallway2 = Room(2,"Beginning of the hallway",None)
F0hallway3 = Room(3,"End of the hallway",None)

F0bathroom = Room(4,"Bathroom",None)

F0livingRoom = Room(5,"Living Room",None)
F0diningRoom = Room(6,"Dining Room",None)

F0entrance = Room(7,"Entrance",None)

F0hallway8 = Room(8,"Beginning of the hallway",None)
F0hallway9 = Room(9,"End of the hallway",None)
F0basementEntrance = Room(10,"Basement entrance",None)