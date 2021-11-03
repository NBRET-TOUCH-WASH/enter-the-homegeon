"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § Amplify weapons on Wallhammer.

    % FIXME:
        % L-125
            % MAKE IT SO THE SCREEN CLEARS WHILE LETTING THE ERROR MESSAGE

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
#from time import sleep


import libs.display.display as display

import libs.maps.maps as maps

import libs.state_machine.state_machine as state_machine

import libs.movement.move as move
import libs.observ.observ as observ


#libs setup


#classes


#functions


#script
actionMenu = """
Select an Action:
1 - Move
2 - Look around (searches the room for objects)
X - WIP
"""


userActionChoiceLoop = True

playerFloor = 1#?1 = upper floor ; 0 = ground floor ; -1 = basement ; (...)
playerRoom = 1


while True:
    display.clearConsole()

    if playerFloor == 1:
        print(maps.FirstFloorMap)
    elif playerFloor == 0:
        print(maps.GroundFloorMap)
    elif playerFloor == -1:
        print("WIP")

    print("Current Location:\n{}\n\n".format(state_machine.state_machine(playerRoom,playerFloor)))


    while userActionChoiceLoop == True:#% TOFIX
        try:
            actionUserChoice = int(input("{}\n> ".format(actionMenu)))
            break
        except ValueError:
            print("Invalid Action choice.")
            continue


    if actionUserChoice == 1:
        playerRoom = move.movement(input("Where do you want to go? ('N'/'S'/'E'/'W')\n> "),playerRoom,playerFloor)

        if playerRoom == "GOTOF1":
            playerRoom = 8
            playerFloor = 1
        elif playerRoom == "GOTOF0":
            playerRoom = 1
            playerFloor = 0
    elif actionUserChoice == 2:
        observ.look_around(playerRoom,playerFloor)
        input("")