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

    $ LOGS: (d/m/y)
        $ 28/10/2021
            $ 00:13AM
                $ hey so i just finished this very basic
                $ movement component and it's basically
                $ what the teachers gave us as an example
                $ so i feel like shit
                $
                $ yeah i had a really hard time doing this
                $ simple thing and i really don't know why
                $
                $ i feel like im so bad at coding it makes
                $ me kinda sad when i see others whip out
                $ crazy shit in seconds
                $ like i got 16/20 at the latest test, and
                $ i haven't seen the programming mark yet! D:
                $
                $ im afraid people will view me as someone
                $ that's not really good at actual programming
                $ whereas I KNOW i can do better, I KNOW
                $ im not that bad
                $
                $ idk maybe im just pressuring myself too much
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
"""


#encoding
#coding:utf-8


#libraries/modules


#libs setup


#classes


#functions
def movement(direction, argPlayerRoom):
    if direction == "n":
        if argPlayerRoom == 1 or argPlayerRoom == 4 or argPlayerRoom == 6 or argPlayerRoom == 10:
            print("invalid\n")
            return argPlayerRoom
        if argPlayerRoom == 2:
            print("room1")
            return 1
        if argPlayerRoom == 3:
            print("room2")
            return 2
        if argPlayerRoom == 5:
            print("room6")
            return 6
        if argPlayerRoom == 7:
            print("room5")
            return 5
        if argPlayerRoom == 8:
            print("room9")
            return 9
        if argPlayerRoom == 9:
            print("room10")
            return 10

    if direction == "s":
        if argPlayerRoom == 1:
            print("room2\n")
            return 2
        if argPlayerRoom == 2:
            print("room3")
            return 3
        if argPlayerRoom == 3 or argPlayerRoom == 4 or argPlayerRoom == 7 or argPlayerRoom == 8:
            print("invalid")
            return argPlayerRoom
        if argPlayerRoom == 5:
            print("room7")
            return 7
        if argPlayerRoom == 6:
            print("room5")
            return 5
        if argPlayerRoom == 9:
            print("room8")
            return 8
        if argPlayerRoom == 10:
            print("room9")
            return 9

    if direction == "e":
        if argPlayerRoom == 1 or argPlayerRoom == 4 or argPlayerRoom == 5 or argPlayerRoom == 6 or argPlayerRoom == 8 or argPlayerRoom == 9:
            print("invalid\n")
            return argPlayerRoom
        if argPlayerRoom == 2:
            print("room5")
            return 5
        if argPlayerRoom == 3:
            print("room4")
            return 4
        if argPlayerRoom == 7:
            print("room8")
            return 8
        if argPlayerRoom == 10:
            print("oob")
            return 0

    if direction == "w":
        if argPlayerRoom == 1 or argPlayerRoom == 2 or argPlayerRoom == 3 or argPlayerRoom == 6 or argPlayerRoom == 7 or argPlayerRoom == 9 or argPlayerRoom == 10:
            print("invalid\n")
            return argPlayerRoom
        if argPlayerRoom == 4:
            print("room3")
            return 3
        if argPlayerRoom == 5:
            print("room2")
            return 2
        if argPlayerRoom == 8:
            print("room7")
            return 7


#script
playerRoom = 1

menu = """
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


while True:
    print(menu)
    playerRoom = movement(input("direction\n> "),playerRoom)