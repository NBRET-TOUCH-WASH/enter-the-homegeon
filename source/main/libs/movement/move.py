"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § 29/10/2021
            § 10:39PM
                § change spacing between '¤' (currency symbol) and item

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


#libs setup


#classes


#functions
def movement(direction, argPlayerRoom, argPlayerFloor):
    if argPlayerFloor == 1:#? UPPER FLOOR
        if direction == "n":
            if argPlayerRoom == 1 or argPlayerRoom == 3 or argPlayerRoom == 4 or argPlayerRoom == 8:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 2:
                return 1
            if argPlayerRoom == 5:
                return 2
            if argPlayerRoom == 6:
                return 3
            if argPlayerRoom == 7:
                return 4

        if direction == "s":
            if argPlayerRoom == 5 or argPlayerRoom == 6 or argPlayerRoom == 7:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 1:
                return 2
            if argPlayerRoom == 2:
                return 5
            if argPlayerRoom == 3:
                return 6
            if argPlayerRoom == 4:
                return 7
            if argPlayerRoom == 8:
                return "GOTOF0"

        if direction == "e":
            if argPlayerRoom == 1 or argPlayerRoom == 5 or argPlayerRoom == 6 or argPlayerRoom == 7 or argPlayerRoom == 8:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 2:
                return 3
            if argPlayerRoom == 3:
                return 4
            if argPlayerRoom == 4:
                return 8

        if direction == "w":
            if argPlayerRoom == 1 or argPlayerRoom == 5 or argPlayerRoom == 6 or argPlayerRoom == 7 or argPlayerRoom == 2:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 3:
                return 2
            if argPlayerRoom == 4:
                return 3
            if argPlayerRoom == 8:
                return 4

        if direction != "n" or direction != "s" or direction != "e" or direction != "w":
            print("Invalid Movement.")
            return argPlayerRoom

    if argPlayerFloor == 0:#? GROUND FLOOR
        
        if direction == "n":
            if argPlayerRoom == 1:
                return "GOTOF1"
            if argPlayerRoom == 4 or argPlayerRoom == 6 or argPlayerRoom == 10:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 2:
                return 1
            if argPlayerRoom == 3:
                return 2
            if argPlayerRoom == 5:
                return 6
            if argPlayerRoom == 7:
                return 5
            if argPlayerRoom == 8:
                return 9
            if argPlayerRoom == 9:
                return 10

        if direction == "s":
            if argPlayerRoom == 1:
                return 2
            if argPlayerRoom == 2:
                return 3
            if argPlayerRoom == 3 or argPlayerRoom == 4 or argPlayerRoom == 7 or argPlayerRoom == 8:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 5:
                return 7
            if argPlayerRoom == 6:
                return 5
            if argPlayerRoom == 9:
                return 8
            if argPlayerRoom == 10:
                return 9

        if direction == "e":
            if argPlayerRoom == 1 or argPlayerRoom == 4 or argPlayerRoom == 5 or argPlayerRoom == 6 or argPlayerRoom == 8 or argPlayerRoom == 9:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 2:
                return 5
            if argPlayerRoom == 3:
                return 4
            if argPlayerRoom == 7:
                return 8
            if argPlayerRoom == 10:
                print("WIP\n")
                return 0

        if direction == "w":
            if argPlayerRoom == 1 or argPlayerRoom == 2 or argPlayerRoom == 3 or argPlayerRoom == 6 or argPlayerRoom == 7 or argPlayerRoom == 9 or argPlayerRoom == 10:
                print("Invalid movement.\nTry again\n")
                return argPlayerRoom
            if argPlayerRoom == 4:
                return 3
            if argPlayerRoom == 5:
                return 2
            if argPlayerRoom == 8:
                return 7

        if direction != "n" or direction != "s" or direction != "e" or direction != "w":
            print("Invalid Movement.")
            return argPlayerRoom



#script