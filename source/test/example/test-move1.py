"""
notes:
    ? docs:
        ? unused file, do not use/read/overwrite/modify in general!!!

        ? Game
            ? goal
                ? player must get to the basement entrance
            ? functionning
                ? player must be able to see map whe nmove has been done

    § TODO:
        § Amplify weapons on Wallhammer.

    % FIXME:
        % Target compromised: move in, move in.

        & FIX:
            & Overwatch, target one sterilized.

    µ WHYNOT:
        µ replace room variables by dics?
            µ (i of course meant "dictionnaries", you naughty reader!)

    ! IMPORTANT:
        ! ⠄⠄⠄⠄⠄⠄⠄⠄⠄⡔⠲⠶⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⠄⠄⠄⣘⡗⠔⡐⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⠄⠄⠄⣨⣿⣠⠐⠞⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⡠⠔⢺⣿⢛⣿⣿⢄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⣤⡶⠡⣲⢀⡴⢟⡻⡛⠓⠴⡾⣷⣱⡀⠄⠄⠄⠄⠄⠄
        ! ⠄⠘⣟⣏⢤⣽⣷⣦⣴⡴⠤⠄⣰⣶⣟⣏⣈⠐⣀⠄⠄⠄⠄
        ! ⠄⠄⢹⣿⣤⢸⣿⣿⣿⣿⣻⣿⣿⡿⠙⠿⣷⣶⣤⠥⠦⠄⠄
        ! ⠄⠄⠘⣿⣷⣤⢚⣿⡿⠿⠿⠛⢛⡨⣥⣤⡈⠙⢻⠶⠧⠄⠄
        ! ⠄⠄⠄⠙⢿⣿⣿⣧⣤⣤⣾⣿⢿⣯⠹⣻⡝⣰⣷⣶⡿⠃⠄
        ! ⠄⠄⠄⠄⠈⠻⣿⡿⢿⣿⣻⣞⣿⠿⠷⢀⡔⢫⡿⠋⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⠸⣿⣿⣿⣯⢿⣦⣄⣘⣒⣛⠶⠊⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⠄⣿⣿⡿⢻⣿⢟⣷⣭⣽⣿⣷⡄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⢀⣴⢿⣿⣿⠯⠺⢾⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⢩⣿⣿⣿⣴⣮⣽⣿⣿⣿⣿⣿⢣⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣆⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⢘⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⡿⠁⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣟⣋⠛⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣧⠺⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⢻⣿⣽⠤⡬⠋⠙⢿⣦⣀⡀⢄⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⠄⡘⣛⣭⣿⠂⠄⠄⠄⠉⠉⠋⠉⠄⠄⠄⠄⠄⠄
        ! ⠄⠄⠄⠄⡔⠄⢀⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        !
        ! "OI JOSUKE, I TOUCHED THIS UNUSED, NEVER SUPPOSED
        ! TO BE OPENED AND MOST PROBABLY RADIOACTIVE FILE
        ! WITH 『ZA HANDO』 AND ACCIDENTALLY REMOVED THE PROTECTION
        ! KEEPING ANYONE FROM READING IT!
        !
        ! NOW THE READER IS GETTING IRRADIATED AND I HAVE A TUMOR
        ! DOWN MY SPINE, AS WELL AS A TERMINAL-STAGE CANCER!
        !
        ! COULD YOU USE 『CRAZY DIAMOND』 TO FIX ALL THIS MESS JOSUKE?
        ! PLEASE???"

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
        if argPlayerRoom == 2:
            print("room 1")
            argPlayerRoom = 1
        if argPlayerRoom == 3:
            print("room2")
            argPlayerRoom = 2
        if argPlayerRoom == 5:
            print("room6")
            argPlayerRoom = 6
        if argPlayerRoom == 7:
            print("room5")
            argPlayerRoom = 5
        if argPlayerRoom == 8:
            print("room9")
            argPlayerRoom = 9
        if argPlayerRoom == 9:
            print("room10")
            argPlayerRoom = 10

    if direction == "s":
        if argPlayerRoom == 1:
            print("room2\n")
            argPlayerRoom = 2
        if argPlayerRoom == 2:
            print("room3")
            argPlayerRoom = 3
        if argPlayerRoom == 3 or argPlayerRoom == 4 or argPlayerRoom == 7 or argPlayerRoom == 8:
            print("invalid")
        if argPlayerRoom == 5:
            print("room7")
            argPlayerRoom = 7
        if argPlayerRoom == 9:
            print("room8")
            argPlayerRoom = 8
        if argPlayerRoom == 10:
            print("room9")
            argPlayerRoom = 9
    
    return argPlayerRoom


#script
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
"""

while True:
    print(menu)
    playerRoom = 2
    playerRoom = movement(input("direction"),playerRoom)