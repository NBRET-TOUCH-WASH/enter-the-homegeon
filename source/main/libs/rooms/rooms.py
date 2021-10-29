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
class Room():
    def __init__(self,number,name,*objects):
        self.number = number
        self.name = name
        self.objects = objects


#functions


#script
downStairs = Room(1,"Bottom of the staircase",None)#all objects currently set to None for safety, as idk what i want to add to rooms yet
hallway2 = Room(2,"Beginning of the hallway",None)
hallway3 = Room(3,"End of the hallway",None)

bathroom = Room(4,"Bathroom",None)

livingRoom = Room(5,"Living Room",None)
diningRoom = Room(6,"Dining Room",None)

entrance = Room(7,"Entrance",None)

hallway8 = Room(8,"Beginning of the hallway",None)
hallway9 = Room(9,"End of the hallway",None)
basementEntrance = Room(10,"Basement entrance",None)