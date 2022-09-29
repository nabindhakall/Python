#!/usr/bin/python3
import random

#Declare floors with rooms and its contents.
from struct import pack


floor_2 = ['nothing', 'stairs down', 'monster', 'magic stones', 'sword']
floor_1 = ['stairs up', 'sword', 'stairs down', 'monster', 'sword']
ground_floor = ['sword', 'stairs up', 'sword', 'moster', 'boss']

#initial position of user
current_floor = floor_2
current_room = 0

#declaring variables
player_won = False
player_alive = True
fighterbag = []

#while loop of the whole game
while player_alive and player_won == False:
    print("You are in a room. There is", current_floor[current_room], "in the room.")

#asking user whats the next move.
    current_move = input("Where would you like to go? \n")

#if statement when the user types left
    if current_move == "left":
        if current_room == 0:
            print("You cannot move left. Please try another direction.")
        elif current_floor[current_room] == "monster":
            print("You try to run away from the monster.")
            if random.randint(0, 10) > 4:
                print("You successfully run away from the monster!")
                current_room = current_room -1
        else:
            print("The monster stabs you before you can get away.")
            player_alive = False

#if statement when the user types right
    elif current_move == "right":
        if current_room == 4:
            print("You can not move right becuase there is no outlet. Please try another direction")
        elif current_floor[current_room] == "monster":
            print("You try to run away from the monster.")
            if random.randint(0, 10) > 4:
                print("You successfully run away from the monster!")
                current_room = current_room + 1
        else:
            print("The monster stabs you before you can get away.")
            player_alive = False

#if statement when the user types up
    elif current_move == "up":
        if current_floor[current_room] != 'stairs up':
            print("There are no stairs thats going up in this room. You can not go up.")
        else: 
            if current_floor == ground_floor:
                current_floor = floor_1
            elif current_floor == floor_1:
                current_floor = floor_2

#if statement when the user types down
    elif current_move == "down":
        if current_floor[current_room] != 'stairs down':
            print("There are no stairs thats going down in this room. You can not go down.")
        else:
            if current_floor == floor_2:
                current_floor = floor_1
            elif current_floor == floor_1:
                current_floor = ground_floor

#if statement when the user types grab
    elif current_move == "grab":
        if len(fighterbag) >= 3:
            print("The Fighter Bag is full. You can not carry anymore items. ")
        else:
            if current_floor[current_room] != "sword" and current_floor[current_room] != "magic stones":
                print("There is nothing you can pick up in this room.")
            else:
                print("You have picked up a", current_floor[current_room])
                fighterbag.append(current_floor[current_room])
                current_floor[current_room] = "nothing"
                print("Now you have", fighterbag, "in your fighterbag.")


#if statement when the user types fight
    elif current_move == "fight":
        if current_floor[current_room] == "monster":
            if "sword" in fighterbag:
                print("You killed the monster with your sword. Monster is dead")
                current_floor[current_room] = "nothing"
                fighterbag.remove("sword")
            else:
                player_alive = False
                print("The monster killed you. Game Over")
        elif current_floor[current_room] == "boss":
            if ("sword" in fighterbag) and ("magic stones" in fighterbag):
                print("You killed the boss with your sword and magic stones. The boss is dead")
                current_floor[current_room] = "nothing"
                fighterbag.remove("sword")
                fighterbag.remove("magic stones")
                player_won = True
            else:
                player_alive = False
                print("The monster killed you. Game Over")

        else:
            print("Sorry, there is no monster here.")    


#if statement when the user types help
    elif current_move == "help":
        print('Type left to go to left room')
        print("Type right to go to the right room")
        print("Type up and down to go either to next floor or down to next floor.")
        print("Type quit to exit out of the game")

#if statement when the user types quit
    elif current_move == "quit":
        current_floor == floor_2
        current_room == 0
        print("You have exited out of the game. Sad to see you go.")
        break

#if the user types any other than "right" "left" "up" "down" "grab" "fight" "help" "quit"
    else:
        print("Sorry, you have entered invalid response. Please enter valid response. Type 'help' if you are stuck.")

#The result of the game Win or Lose.
if player_won:
    print("Congtaulations you have won the game.")
if player_alive == False:
    print("Sorry, you have been killed and you lost the game. Better luck next time.")