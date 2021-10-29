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
import libs.state_machine.state_machine as state_machine
import libs.observ.observ as observ
import libs.movement.move as move


#libs setup


#classes


#functions


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
    print("Current Location:\n{}\n".format(state_machine.state_machine(playerRoom)))
    playerRoom = move.movement(input("Where do you want to go? ('N'/'S'/'E'/'W')\n> "),playerRoom)