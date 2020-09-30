#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math
import time

cmp_number = 0
choose_range = 100
max_count = 7
count = 0

message = "Welcome to guess100"


def new_game():
    
    global cmp_number, choose_range, count,message
    cmp_number = random.randrange(0, choose_range)
    count = 0
    print ("")
    print("New game, Range is from 0 to", choose_range)
    print("Number of remaining guesses is", max_count)
    print("")
    


def range10():
    
    global choose_range, max_count,message
    choose_range = 10
    max_count = int(math.ceil(math.log(choose_range, 2)))
    message = "Welcome to guess10"
    new_game()


def range100():
   
    global choose_range, max_count,message
    choose_range = 100
    max_count = int(math.ceil(math.log(choose_range, 2)))
    message = "Welcome to guess100"
    new_game()


def range1000():
    
    global choose_range, max_count,message
    choose_range = 1000
    max_count = int(math.ceil(math.log(choose_range, 2)))
    message = "Welcome to guess1000"
    new_game()

    
def input_guess(guess):
    
    global max_count, count,message
    int_guess = int(guess)
    print ("Guess was" , int_guess)
    count = count + 1
    if count < max_count and int_guess != cmp_number:
        if int_guess > cmp_number:
            print ("Number of remaining guesses is " , max_count - count)
            print ("your guess is Higher!")
            
            message = "higher!   remaining try:"+str(max_count - count)
        else:
            print ("Number of remaining guesses is " , max_count - count)
            print("Your guess is Lower!")
            
            message = "lower!  remaining try:"+str(max_count - count)
    elif count <= max_count and int_guess == cmp_number:
        print ("Correct! The number was", cmp_number)
        print ("And it only took you", count, "tries!")
        message = "correct! you are in new game"
        new_game()
        
        
        
        
    else:
        print ("Number of remaining guesses is " , max_count - count)
        print("You ran out of guesses. The number was", cmp_number)
        
        message = "nope!! you lose!"+"The number was"+str(cmp_number)
        new_game()
def draw(canvas):
    global max_count
    canvas.draw_text(message, [50,112], 36, "green")
    canvas.draw_text("total try"+str(max_count), [400,20], 20, "cyan")
def msg():
    global message
    message = "Good job!"
    

frame = simplegui.create_frame("Guessing game", 500, 400)


frame.add_button("Range is [0, 10)", range10, 200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_button("start a new game", new_game, 200)
frame.add_input("Enter your guess", input_guess, 200)
frame.set_draw_handler(draw)




frame.start()

