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
        return "[{}] {}".format(rooms.downStairs.number,rooms.downStairs.name)
    if argCurrentRoom == 2:
        return "[{}] {}".format(rooms.hallway2.number,rooms.hallway2.name)
    if argCurrentRoom == 3:
        return "[{}] {}".format(rooms.hallway3.number,rooms.hallway3.name)
    if argCurrentRoom == 4:
        return "[{}] {}".format(rooms.bathroom.number,rooms.bathroom.name)
    if argCurrentRoom == 5:
        return "[{}] {}".format(rooms.livingRoom.number,rooms.livingRoom.name)
    if argCurrentRoom == 6:
        return "[{}] {}".format(rooms.diningRoom.number,rooms.diningRoom.name)
    if argCurrentRoom == 7:
        return "[{}] {}".format(rooms.entrance.number,rooms.entrance.name)
    if argCurrentRoom == 8:
        return "[{}] {}".format(rooms.hallway8.number,rooms.hallway8.name)
    if argCurrentRoom == 9:
        return "[{}] {}".format(rooms.hallway9.number,rooms.hallway9.name)
    if argCurrentRoom == 10:
        return "[{}] {}".format(rooms.basementEntrance.number,rooms.basementEntrance.name)
        #print("You are at the end of the hallway.\nIn front of you is the door leading down the basement. [10]")


#script