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
        $ 29/10/2021
            $ XY:ABCPM
"""


#encoding
#coding:utf-8


#libraries/modules
import libs.rooms.rooms as rooms


#libs setup


#classes


#functions
def movement(direction, argPlayerRoom):
    if direction == "n":
        if argPlayerRoom == 1 or argPlayerRoom == 4 or argPlayerRoom == 6 or argPlayerRoom == 10:
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


#script
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
"""