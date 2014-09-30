# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# write import statements
import math
import random
import simplegui

# define global variables
num_range = 100
guesses_remaining = 0
secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range, guesses_remaining, secret_number
    guesses_remaining = int(math.ceil(math.log((num_range - 0), 2)))
    secret_number = random.randrange(0, num_range)
    print "\nNew game. Range is from 0 to", num_range
    print "Number of remaining guesses is", guesses_remaining

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global guesses_remaining
    print "\nGuess was", guess
    guess = int(guess)
    guesses_remaining -= 1
    print "Number of remaining guesses is", guesses_remaining
    # main game logic goes here
    if guesses_remaining > 0:
        if guess > secret_number:
            print "Lower"
        elif guess < secret_number:
            print "Higher"
        else:
            print "Correct"
            new_game()
    else:
        if guess == secret_number:
            print "Correct"
        else:
            print "You ran out of guesses. The number was", secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

# call new_game 
new_game()