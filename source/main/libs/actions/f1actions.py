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
        µ add more actions?

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



#libs setup


#classes


#functions
#[1]
def bedroom_jump_from_window():
    print("\nYou open the bedroom's only window and stand proudly in its frame.\nYou take a light breath and jump to what seems like your death.\n")
    time.sleep(3.0)

    print("SNAP!\nAs you land straight as a nail on the pavement's concrete right below, you break both of your legs!\n")
    time.sleep(3.0)

    print("You slowly bleed out, your kneecaps and femurs protruding through your legs.\n")

    time.sleep(1.5)
    #input("(press any key to continue...) > ")

    return "PLAYERISDEAD"

#[2]

#[3]

#[4]

#[5]
def sibling_change_clothes():
    print("\nYou open the closet and change your clothes.\n")
    time.sleep(2.0)

    print("Unfortunately, this is a text-based adventure, meaning you have to imagine your character in a new outfit from now on...\n")
    time.sleep(3.0)

    print("Here, help to visualize it:\n")
    time.sleep(1.0)
    print(""" ☺
/T\\\t<- You
 /\\
""")

    time.sleep(1.5)
    #input("(press any key to continue...) > ")

#[6]

#[7]
def restrooms_flush():
    print("\nYou flush the toilet.")
    time.sleep(1.0)
    print("Great.\n")

    time.sleep(1.5)
    #input("(press any key to continue...) > ")

def restrooms_use():
    print("\n1 - Small \"need\"\n2 - Big \"need\"\n")
    restroomUseChoice = int(input("What do you want to use the toilet for?\n> "))

    if restroomUseChoice == 1:
        print("\nYou use the toilet.")
        time.sleep(1.0)
        print("Not much more to that.\n")
    elif restroomUseChoice == 2:
        print("\nYou REALLY USE the toilet.")
        time.sleep(1.0)
        print("Nothing more to that.\n")

    time.sleep(1.5)
    #input("(press any key to continue...) > ")

def restrooms_drink():
    print("\nYou drink the\nh o l y   b e v e r a g e . . . \n")
    time.sleep(2.0)
    print("It tastes like [REDACTED].\n")

    time.sleep(1.5)
    #input("(press any key to continue...) > ")

#[8]


#script