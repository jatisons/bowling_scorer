# File: bowling_sim.py
# Description: Generates an array representing a game of bowling. Used 
#              to test bowling_OO.py and bowling_functional.py
# By: Jesse Smith

import random

# Generates first roll of bowling game
def roll_1():
    return random.randint(0,10)

# Generates second roll of bowling game based on remaining pins from first roll
def roll_2(first):
    return random.randint(0,10 - first)    

# Simulates a bowling game
def sim_game():
    frames_created = 0
    game = []
    # Only generate 10 frames, roll once, if its a strike add to list, if not a strike take second roll
    while frames_created != 10:
        first_roll = roll_1()
        if first_roll == 10:
            game.append(first_roll)
        else:
            game.extend((first_roll,roll_2(first_roll)))
        frames_created += 1
    # If done generating the standard 10 frames, check the last roll for a strike, if strike allow two more rolls
    # Check the last two rolls for a spare, if spare allow one more roll
    if frames_created == 10:
        if game[-1] == 10:
            game.extend((roll_1(),roll_1()))
        elif sum(game[-2:]) == 10:
            game.append(roll_1())
    return game        
