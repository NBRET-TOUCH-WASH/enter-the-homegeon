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
import time


import libs.display.display as display



#libs setup


#classes


#functions
def game_over():
    display.clearConsole()
    print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \\
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\\\n""")
    time.sleep(2.0)
    print("\" It's a sad thing that your adventures have ended here!! \"\n\t- Shadowgate (NES), 1989\n")

    time.sleep(1.5)
    input("(press any key to continue...) > ")


#script