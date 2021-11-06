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
        $ 28/10/2021
            $ Ready weapons, stay alert.
"""


#encoding
#coding:utf-8


#libraries/modules
import sys
import os
import time


#libs setup


#classes


#functions
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def ending():
    clearConsole()

    print(congrats)
    time.sleep(2.0)
    print(congratsTxt)
    time.sleep(1.5)
    input("(press any key to continue...) > ")

    sys.exit(0)


#script
congrats = """
   ______                             __        __      __  _                  __
  / ____/___  ____  ____ __________ _/ /___  __/ /___ _/ /_(_)___  ____  _____/ /
 / /   / __ \/ __ \/ __ `/ ___/ __ `/ __/ / / / / __ `/ __/ / __ \/ __ \/ ___/ / 
/ /___/ /_/ / / / / /_/ / /  / /_/ / /_/ /_/ / / /_/ / /_/ / /_/ / / / (__  )_/  
\____/\____/_/ /_/\__, /_/   \__,_/\__/\__,_/_/\__,_/\__/_/\____/_/ /_/____(_)   
                 /____/                                                          \n
"""

congratsTxt = """

Congratulations!
You have achieved <Enter the HomeGeon>'s ending!

Thank you for playing!
I hope this wasn't too disappointing or anything of the sort...

Aside from a few actions you may have missed, there's not much more to the game now.
Unless...

"""