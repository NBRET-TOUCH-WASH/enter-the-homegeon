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


#libs setup


#classes


#functions
def state_machine(argCurrentRoom):
    if argCurrentRoom == 1:
        print("You are at the bottom of the staircase. [1]\n")
    if argCurrentRoom == 2:
        print("You are at the beginning of the hallway. [2]\n")
    if argCurrentRoom == 3:
        print("You are at the end of the hallway. [3]\n")
    if argCurrentRoom == 4:
        print("You are in the bathroom. [4]\n")
    if argCurrentRoom == 5:
        print("You are in the living room. [5]\n")
    if argCurrentRoom == 6:
        print("You are in the dining room. [6]\n")
    if argCurrentRoom == 7:
        print("You are in the entrance.\nIn front of you is the front door. [7]\n")
    if argCurrentRoom == 8:
        print("You are at the beginning of the hallway. [8]\n")
    if argCurrentRoom == 9:
        print("You are in the middle of the hallway. [9]\n")
    if argCurrentRoom == 10:
        print("You are at the end of the hallway.\nIn front of you is the door leading down the basement. [10]\n")


#script