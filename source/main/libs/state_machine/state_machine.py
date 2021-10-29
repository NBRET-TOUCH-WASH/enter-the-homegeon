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
        µ Overwatch reports possible hostiles inbound.

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ Ready weapons, stay alert.
"""

"""
 o
 |
[1] [  6  ] [10]-o
 |   |   |   |
 |   |   |   |
[2]-[  5  ] [9 ]
 |       |   |
[3]-[4] [7]-[8 ]
         |
         o
\n
"""


#encoding
#coding:utf-8


#libraries/modules
import libs.rooms.rooms as rooms


#libs setup


#classes


#functions
def state_machine(argCurrentRoom):
    if argCurrentRoom == 1:
        return "{} [{}]\n".format(rooms.downStairs.name,rooms.downStairs.number)
    if argCurrentRoom == 2:
        return "{} [{}]\n".format(rooms.hallway2.name,rooms.hallway2.number)
    if argCurrentRoom == 3:
        return "{} [{}]\n".format(rooms.hallway3.name,rooms.hallway3.number)
    if argCurrentRoom == 4:
        return "{} [{}]\n".format(rooms.bathroom.name,rooms.bathroom.number)
    if argCurrentRoom == 5:
        return "{} [{}]\n".format(rooms.livingRoom.name,rooms.livingRoom.number)
    if argCurrentRoom == 6:
        return "{} [{}]\n".format(rooms.diningRoom.name,rooms.diningRoom.number)
    if argCurrentRoom == 7:
        return "{} [{}]\n".format(rooms.entrance.name,rooms.entrance.number)
    if argCurrentRoom == 8:
        return "{} [{}]\n".format(rooms.hallway8.name,rooms.hallway8.number)
    if argCurrentRoom == 9:
        return "{} [{}]\n".format(rooms.hallway9.name,rooms.hallway9.number)
    if argCurrentRoom == 10:
        return "{} [{}]\n".format(rooms.basementEntrance.name,rooms.basementEntrance.number)
        #print("You are at the end of the hallway.\nIn front of you is the door leading down the basement. [10]\n")


#script