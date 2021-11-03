"""
notes:
    ? docs:
        ? Display-related content

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
        $ Ready weapons, stay alert.
"""


#encoding
#coding:utf-8


#libraries/modules
import os


#libs setup


#classes


#functions
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#script