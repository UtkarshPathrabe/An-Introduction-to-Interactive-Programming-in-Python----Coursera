# Rock-paper-scissors-lizard-Spock program

import math
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

#assign name to given number
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    return number

#assign number to given name
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    return name
    

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(computer_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + computer_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = ((player_number - computer_number) % 5)
    
    # use if/elif/else to determine winner, print winner message
    if difference == 1 or difference == 2:
        print "Player wins!"
    elif difference == 3 or difference == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    return ""
    

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric