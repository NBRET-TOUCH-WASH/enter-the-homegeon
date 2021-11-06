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
        µ f1actions.py
            µ add more actions?

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
        $ 03/11/2021
            $ 10:41PM
                $ i think im gonna completely change the way im headed with this project
                $ and turn this into a shadowgate-like game lmao
"""


#encoding
#coding:utf-8


#libraries/modules
import time
import sys


#import libs.game_states.endings.true_ending as true_ending

import libs.game_states.game_states as game_states
import libs.actions.player_actions as player_actions

import libs.ui.menus.title_screen.title_screen as title_screen
import libs.ui.menus.title_screen.about as about
import libs.display.display as display
import libs.maps.maps as maps

import libs.state_machine.state_machine as state_machine

import libs.movement.move as move
import libs.observ.observ as observ

import libs.inventory.inventory as inventory
import libs.game_states.endings.true_ending as ending
import libs.game_states.endings.ending as reg_ending


#libs setup


#classes


#functions


#script
actionMenu = """
Select an Action:
1 - Move
2 - Investigate the room
X - WIP
"""

roomActionsMenu = """
What do you want to do in this room?
1 - Look for objects
2 - Look for available actions
X - WIP
"""



userActionChoiceLoop = True
userChosenActionLoop = True

playerFloor = 1#?1 = upper floor ; 0 = ground floor ; -1 = basement ; (...)
playerRoom = 1

hasBasementKey = False
hasEntranceKey = False


while True:
    display.clearConsole()
    userTitleChoice = int(input("{}{}> ".format(title_screen.titleTxt,title_screen.titleOptions)))

    if userTitleChoice == 1:
        newGameLaunched = True
        while newGameLaunched == True:
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
                elif playerRoom == "GOTOOUT":
                    playerRoom = 1
                    playerFloor = None
                    time.sleep(2.0)
                    print("As you open the door, a meteorite hits you in the face blowing up both your house and your face.\n")
                    time.sleep(4.0)
                    reg_ending.ending()
                    newGameLaunched = False
                elif playerRoom == "GOTOFDASH1":
                    playerRoom = 1
                    playerFloor = -1
                    ending.true_ending()
                    newGameLaunched = False

            elif actionUserChoice == 2:
                try:
                    actionMenuChoice = observ.look_around(int(input("{}\n> ".format(roomActionsMenu))),playerRoom,playerFloor)
                except:
                    continue

                if actionMenuChoice == 1:
                    if (playerRoom == 7 and playerFloor == 1) or (playerRoom == 4 and playerFloor == 0):
                        objectTaken = inventory.get_object(playerRoom,playerFloor)
                    else:
                        objectTaken = None
                    if objectTaken == "HASBASEMENTKEY":
                        move.canOpenBasement = True
                    elif objectTaken == "HASENTRANCEKEY":
                        move.canOpenEntrance = True
                    elif objectTaken == None:
                        pass
                elif actionMenuChoice == 2:
                    if (playerRoom == 1 and playerFloor == 1) or (playerRoom == 5 and playerFloor == 1) or (playerRoom == 7 and playerFloor == 1) or (playerRoom == 2 and playerFloor == 0) or (playerRoom == 4 and playerFloor == 0) or (playerRoom == 6 and playerFloor == 0):
                        while userChosenActionLoop == True:
                            try:
                                playerChosenAction = player_actions.choose_action(int(input("Select an available action:\n> ")),playerRoom,playerFloor)
                                break
                            except:
                                print("\nInvalid Action Choice.\n")
                                continue
                    else:
                        playerChosenAction = None
                    if playerChosenAction == "PLAYERISDEAD":
                        game_states.game_over()
                        newGameLaunched = False
                else:
                    pass

                input("\n(press any key to continue...) > ")


    elif userTitleChoice == 2:
        display.clearConsole()
        print(about.aboutSectionTitle,about.aboutSectionTxt)
        input("(press any key to continue...) > ")


    elif userTitleChoice == 3:
        sys.exit(0)