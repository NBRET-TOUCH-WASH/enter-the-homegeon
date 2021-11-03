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



#libs setup


#classes


#functions
def choose_action(argUserChoice,arguserRoom,argUserFloor):
    if argUserFloor == 1:
        if arguserRoom == 1:
            if argUserChoice == 1:
                return f1actions.jump_from_window()


#script