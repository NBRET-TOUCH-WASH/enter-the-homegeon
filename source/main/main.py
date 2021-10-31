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
        $ 29/10/2021
            $ 11:30PM
                $ i think im gonna stop here for today,
                $ im really thriving as of late on this
                $ project and it's making me feel super
                $ good and confident in my abilities again
                $
                ! README: (for my future self) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    $ you just got done with the very basic
                    $ menu stuff (like it prints out n all)
                    $ but you have yet to put it in a separate
                    $ file
                    $
                    $ and you still have to implement:
                    $ (in the basic components category)
                        § inventory
                            § object handling (pick up ; drop(?) ; use ; etc)
                        § a proper UI
                        § sound
                        § floor system
                        § '''''storyline''''', if you can call it that lmao
                        ! BTW YOU HAVE TO MAKE IT SO THAT WHEN THE look_around()
                        ! RETURNS "None" IT SAYS "No Objects in the Room" OR WHATEVER
                    $
                    $ btw i added a fÜnnÎ comment somewhere as usual
                    ! CAREFUL WITH THE MERGING, WE LOST THE OKUYASU ONE CUZ OF IT :(
"""


#encoding
#coding:utf-8


#libraries/modules
import libs.state_machine.state_machine as state_machine

import libs.menu.menu as libmenu

import libs.movement.move as move
import libs.observ.observ as observ


#libs setup


#classes


#functions


#script
FirstFloorMap = """
[1]
 |
[   2   ]-[6]
 |  |  |   |
[3][4][5] (>)
"""

GroundFloorMap = """
(<)
 |
[1] [  6  ] [10]-(>)
 |   |   |   |
 |   |   |   |
[2]-[  5  ] [9 ]
 |       |   |
[3]-[4] [7]-[8 ]
         |
         o
"""

actionMenu = """
Select an Action:
1 - Move
2 - Look around (searches the room for objects)
X - WIP
"""


playerRoom = 1

while True:
    print(GroundFloorMap)
    print("Current Location:\n{}\n\n".format(state_machine.state_machine(playerRoom)))

    actionUserChoice = int(input("{}\n> ".format(actionMenu)))
    if actionUserChoice == 1:
        playerRoom = move.movement(input("Where do you want to go? ('N'/'S'/'E'/'W')\n> "),playerRoom)
    elif actionUserChoice == 2:
        observ.look_around(playerRoom)