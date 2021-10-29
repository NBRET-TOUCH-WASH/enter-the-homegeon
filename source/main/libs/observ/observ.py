"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § 29/10/2021
            § 10:39PM
                § change spacing between '¤' (currency symbol) and item

    % FIXME:
        % Target compromised: move in, move in.

        & FIX:
            & Overwatch, target one sterilized.

    µ WHYNOT:
        µ Overwatch reports possible hostiles inbound.

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ 29/10/2021
            $ 10:29PM
                $ it works! it's the most spaghetti
                $ and stupid my code's been yet but
                $ idc i'll make it more dynamic later
                $ when i get the components down
"""


#encoding
#coding:utf-8


#libraries/modules
import libs.rooms.rooms as rooms


#libs setup


#classes


#functions
def look_around(argPlayerRoom):
    if argPlayerRoom == 1:
        for item in rooms.downStairs.objects:
            print("Items in the room:\n¤    {}".format(item))#§ change spacing
    if argPlayerRoom == 2:
        for item in rooms.hallway2.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 3:
        for item in rooms.hallway3.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 4:
        for item in rooms.bathroom.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 5:
        for item in rooms.livingRoom.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 6:
        for item in rooms.diningRoom.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 7:
        for item in rooms.entrance.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 8:
        for item in rooms.hallway8.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 9:
        for item in rooms.hallway9.objects:
            print("Items in the room:\n¤    {}".format(item))
    if argPlayerRoom == 10:
        for item in rooms.basementEntrance.objects:
            print("Items in the room:\n¤    {}".format(item))


#script
"""
 o
 |
[1] [  6  ] [10]-o
 |   |   |   |
 |   |   |   |
[2]-[  5  ] [9 ]
 |       |   |
[3]-[4] [7]-[8 ]
         |
         o
"""