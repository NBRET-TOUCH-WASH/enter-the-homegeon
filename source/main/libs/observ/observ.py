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
from libs.rooms.rooms import F0basementEntrance, F0bathroom, F0diningRoom, F0downStairs, F0entrance, F0hallway2, F0hallway3, F0hallway8, F0hallway9, F0livingRoom, F1bedroom, F1hallway2, F1hallway3, F1hallway4, F1hallway8, F1parentsRoom6, F1restrooms7, F1siblingRoom5

import libs.inventory.inventory as inventory

#libs setup


#classes


#functions
def look_around(argUserChoice, argPlayerRoom, argPlayerFloor):
    if argUserChoice == 1:
        if argPlayerFloor == 1:
            if argPlayerRoom == 1:
                #for item in rooms.F1bedroom.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))#µ change spacing?
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 2:
                #for item in rooms.F1hallway2.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 3:
                #for item in rooms.F1hallway3.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 4:
                #for item in rooms.F1hallway4.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 5:
                #for item in rooms.F1siblingRoom5.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 6:
                #for item in rooms.F1parentsRoom6.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 7:
                #for item in rooms.F1restrooms7.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                if F1restrooms7.objects != None:
                    print("Items in the room:\n1 - {}".format(F1restrooms7.objects))
                else:
                    print("There are no objects in the room.\n")

            if argPlayerRoom == 8:
                #for item in rooms.F1hallway8.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")

            #if argPlayerRoom != 1 or argPlayerRoom != 2 or argPlayerRoom != 3 or argPlayerRoom != 4 or argPlayerRoom != 5 or argPlayerRoom != 6 or

        if argPlayerFloor == 0:
            if argPlayerRoom == 1:
                #for item in rooms.downStairs.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 2:
                #for item in rooms.hallway2.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 3:
                #for item in rooms.hallway3.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 4:
                #for item in rooms.bathroom.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            #if argPlayerRoom == 5:
            #    for item in rooms.livingRoom.objects:
            #        i = 0
            #        print("Items in the room:\n1 - {}".format(i+1,item))
            #        i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 6:
            #    for item in rooms.diningRoom.objects:
            #        i = 0
            #        print("Items in the room:\n1 - {}".format(i+1,item))
            #        i += 1
                print("There are no objects in the room.\n")#!HEREEEEEEEEEEEEEEE
            if argPlayerRoom == 7:
                #for item in rooms.entrance.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 8:
                #for item in rooms.hallway8.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 9:
                #for item in rooms.hallway9.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")
            if argPlayerRoom == 10:
                #for item in rooms.basementEntrance.objects:
                #    i = 0
                #    print("Items in the room:\n1 - {}".format(i+1,item))
                #    i += 1
                print("There are no objects in the room.\n")

    if argUserChoice == 2:
        if argPlayerFloor == 1:
            if argPlayerRoom == 1:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1bedroom.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 2:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1hallway2.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 3:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1hallway3.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 4:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1hallway4.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 5:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1siblingRoom5.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 6:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1parentsRoom6.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 7:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1restrooms7.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 8:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F1hallway8.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")

        if argPlayerFloor == 0:
            if argPlayerRoom == 1:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0downStairs.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 2:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0hallway2.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 3:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0hallway3.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 4:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0bathroom.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 5:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0livingRoom.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 6:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0diningRoom.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 7:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0entrance.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 8:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0hallway8.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 9:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0hallway9.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")
            if argPlayerRoom == 10:
                print("\nActions available in this room:")
                i = 0
                for action in rooms.F0basementEntrance.actions:
                    print("{} - {}".format(i+1,action))
                    i += 1
                print("")

    return argUserChoice

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