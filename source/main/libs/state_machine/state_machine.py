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


#encoding
#coding:utf-8


#libraries/modules
import libs.rooms.rooms as rooms


#libs setup


#classes


#functions
def state_machine(argCurrentRoom, argCurrentFloor):
    if argCurrentFloor == 1:#? UPPER FLOOR
        if argCurrentRoom == 1:
            return "[{}] {}".format(rooms.F1bedroom.number,rooms.F1bedroom.name)
        if argCurrentRoom == 2:
            return "[{}] {}".format(rooms.F1hallway2.number,rooms.F1hallway2.name)
        if argCurrentRoom == 3:
            return "[{}] {}".format(rooms.F1hallway3.number,rooms.F1hallway3.name)
        if argCurrentRoom == 4:
            return "[{}] {}".format(rooms.F1hallway4.number,rooms.F1hallway4.name)
        if argCurrentRoom == 5:
            return "[{}] {}".format(rooms.F1siblingRoom5.number,rooms.F1siblingRoom5.name)
        if argCurrentRoom == 6:
            return "[{}] {}".format(rooms.F1parentsRoom6.number,rooms.F1parentsRoom6.name)
        if argCurrentRoom == 7:
            return "[{}] {}".format(rooms.F1restrooms7.number,rooms.F1restrooms7.name)
        if argCurrentRoom == 8:
            return "[{}] {}".format(rooms.F1hallway8.number,rooms.F1hallway8.name)


    if argCurrentFloor == 0:#? GROUND FLOOR
        if argCurrentRoom == 1:
            return "[{}] {}".format(rooms.F0downStairs.number,rooms.F0downStairs.name)
        if argCurrentRoom == 2:
            return "[{}] {}".format(rooms.F0hallway2.number,rooms.F0hallway2.name)
        if argCurrentRoom == 3:
            return "[{}] {}".format(rooms.F0hallway3.number,rooms.F0hallway3.name)
        if argCurrentRoom == 4:
            return "[{}] {}".format(rooms.F0bathroom.number,rooms.F0bathroom.name)
        if argCurrentRoom == 5:
            return "[{}] {}".format(rooms.F0livingRoom.number,rooms.F0livingRoom.name)
        if argCurrentRoom == 6:
            return "[{}] {}".format(rooms.F0diningRoom.number,rooms.F0diningRoom.name)
        if argCurrentRoom == 7:
            return "[{}] {}".format(rooms.F0entrance.number,rooms.F0entrance.name)
        if argCurrentRoom == 8:
            return "[{}] {}".format(rooms.F0hallway8.number,rooms.F0hallway8.name)
        if argCurrentRoom == 9:
            return "[{}] {}".format(rooms.F0hallway9.number,rooms.F0hallway9.name)
        if argCurrentRoom == 10:
            return "[{}] {}".format(rooms.F0basementEntrance.number,rooms.F0basementEntrance.name)
            #print("You are at the end of the hallway.\nIn front of you is the door leading down the basement. [10]")


#script