# File: bowling_functional.py
# Description: Functional programming approach to calculating the score of a bowling game
# By: Jesse Smith

# import ordered dict to make iteration easier in scoring without a counter variable
from collections import OrderedDict

# Creates bowling frames from array input
def create_frames(game,open_frame = (),frames = OrderedDict({})):
    # For each roll in the array, if it is less than 10, add to the frame tuple, if its 10 count as strike and append to the frame tuple    
    for roll in game:
        # Accounts for bonus frame roll less than 10 pins
        if roll < 10 and len(frames) == 10:
            open_frame += (roll,)
            frames.update({len(frames)+1: open_frame})
        # Accounts for less than 10 pins or a 0,10 spare frame            
        elif roll < 10 or roll == 10 and len(open_frame) == 1:
            open_frame += (roll,)
            # If after the roll is added to the tuple on last line, look for the max rolls in a frame and add to frames dictionary
            if len(open_frame) == 2:
                frames.update({len(frames)+1: open_frame})
                open_frame = ()
        # if the roll is a strike, add it to the frames dictionary
        elif roll == 10:
            open_frame += (roll,)
            frames.update({len(frames)+1: open_frame})
            open_frame = ()
    return frames
# Scores a strike using the strike, plus the next two rolls
def strike_score(current,bonus1,bonus2):
    # Accounts for strike on bonus roll 
    if len(bonus1) == 1:
        return sum(current) + bonus1[0] + bonus2[0]
    # Accounts for anything other than a strike in the bonus roll
    else:
        return sum(current) + sum(bonus1)
# Scores a spare using the spare, plus the next roll
def spare_score(current,bonus1):
    return sum(current) + bonus1[0]
       
def total_score(frames,total = 0):
    for frame_key, frame in frames.items():
        # Frame 11 is only used for computing bonuses, so stop if we iterate to it
        if frame_key == 11:
            break
        # Accounts for spare bonus or a strike bonus in the last frame
        elif frame_key == 10 and sum(frame) == 10:
            total += strike_score(frame,frames[frame_key+1],[0])
            display_score(frame_key,strike_score(frame,frames[frame_key+1],[0]),total)
        # Accounts for a stike in the 9th frame
        elif frame_key == 9 and frame[0] == 10:
            total += strike_score(frame,frames[frame_key+1],[0])
            display_score(frame_key,strike_score(frame,frames[frame_key+1],[0]),total)
        # Accounts for a strike for the roll
        elif frame[0] == 10:
            total += strike_score(frame,frames[frame_key+1],frames[frame_key+2])
            display_score(frame_key,strike_score(frame,frames[frame_key+1],frames[frame_key+2]),total)
        # Accounts for a spare frame
        elif sum(frame) == 10 and len(frame) == 2:
            total += spare_score(frame,frames[frame_key+1])
            display_score(frame_key,spare_score(frame,frames[frame_key+1]),total)
        # Accounts for an open frame
        else:
            total += sum(frame)
            display_score(frame_key,sum(frame),total)
# Formats a string to display the scoring
def display_score(frame_key,frame_score,running_total): 
    return print("Frame "+str(frame_key)+" score is: "+str(frame_score)+" Total score is: "+str(running_total))  

# Imports the bowling simulator to generate test data
from bowling_sim import sim_game
# Generate test data  
test_game = sim_game()
# Show the input for this run
print("\nThe simulated game is:\n"+str(test_game))
# Test the functions      
test_frame = create_frames(test_game)
# Displays the formatted frames and the scoring for debugging
print("\nFrames created with create_frames():\n"+str(test_frame))
print("\nScore of simulated game:")  
total_score(test_frame)
