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
        µ make a floor list with room class instances, use index with movement()?

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ 28/10/2021
            $ 01:54AM
                $ don't really know where im going with this one
"""


#encoding
#coding:utf-8


#libraries/modules
#import time
import libs.actions.f1actions as f1actions
import libs.actions.f0actions as f0actions



#libs setup


#classes


#functions
def choose_action(argUserChoice,argUserRoom,argUserFloor):
    if argUserFloor == 1:
        if argUserRoom == 1:
            if argUserChoice == 1:
                return f1actions.bedroom_jump_from_window()
        if argUserRoom == 2:
            pass
        if argUserRoom == 3:
            pass
        if argUserRoom == 4:
            pass
        if argUserRoom == 5:
            if argUserChoice == 1:
                return f1actions.sibling_change_clothes()
        if argUserRoom == 6:
            pass
        if argUserRoom == 7:
            if argUserChoice == 1:
                return f1actions.restrooms_flush()
            if argUserChoice == 2:
                return f1actions.restrooms_use()
        if argUserRoom == 8:
            pass

    if argUserFloor == 0:
        if argUserRoom == 1:
            pass
        if argUserRoom == 2:
            if argUserChoice == 1:
                return f0actions.hallway2_observe_painting()
        if argUserRoom == 3:
            pass
        if argUserRoom == 4:
            if argUserChoice == 1:
                return f0actions.bathroom_look_at_mirror()#% make it so the spooky stuff only happens once
            if argUserChoice == 2:
                return f0actions.bathroom_wash_hands()
            if argUserChoice == 3:
                return f0actions.bathroom_pull_curtain()
        if argUserRoom == 5:
            pass
        if argUserRoom == 6:
            if argUserChoice == 1:
                return f0actions.dining_sit()
        if argUserRoom == 7:
            pass
        if argUserRoom == 8:
            pass
        if argUserRoom == 9:
            pass
        if argUserRoom == 10:
            pass

    #input("(press any key to continue...) > ")


#script