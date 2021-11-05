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
        $ 05/11/2021
            $ 09:48PM
                $ i think im gonna go for flags
                $ as of now
                $
                $ maybe make it into
                $ a full inventory in a future
                $ update
"""


#encoding
#coding:utf-8


#libraries/modules
import libs.display.display as display


#libs setup


#classes


#functions
#def show_inventory():
#    print(playerInventory)

def get_object(argPlayerRoom,argPlayerFloor):
    while True:
        hasTakenObject = input("\nTake the object? (y/n)\n> ")

        if (hasTakenObject == "y" or hasTakenObject == "Y") and (argPlayerRoom == 7 and argPlayerFloor == 1):
            return "HASBASEMENTKEY"
        elif hasTakenObject == "n" or hasTakenObject == "N":
            return None
        else:
            pass

        if (hasTakenObject == "y" or hasTakenObject == "Y") and (argPlayerRoom == 6 and argPlayerFloor == 0):
            return "HASENTRANCEKEY"
        elif hasTakenObject == "n" or hasTakenObject == "N":
            return None
        else:
            print("\nInvalid choice. Try again.")
            continue


#script
#playerInventory = ["e"]