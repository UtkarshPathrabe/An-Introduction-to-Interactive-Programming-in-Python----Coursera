# @ Author : Utkarsh Ashok Pathrabe

# Implementation of "Stopwatch: The Game"
import simplegui

# define global variables
IsRunning = False
Counter, GoodStop, TotalStop = 0, 0, 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D, t = t % 10, t / 10
    C, t = t % 10, t / 10
    B, A = t % 6, t / 6
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define helper function score that returns current score
def score():
    return str(GoodStop) + "/" + str(TotalStop)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global IsRunning
    timer.start()
    IsRunning = True

def stop():
    global IsRunning, GoodStop, TotalStop
    timer.stop()
    if IsRunning:
        TotalStop += 1
        if Counter % 10 == 0:
            GoodStop += 1
    IsRunning = False

def reset():
    global IsRunning, GoodStop, TotalStop, Counter
    timer.stop()
    IsRunning = False
    Counter, GoodStop, TotalStop = 0, 0, 0

# define event handler for timer with 0.1 sec interval
def tick():
    global Counter
    Counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(Counter), [60, 85], 36, "White")
    canvas.draw_text(score(), [155, 25], 26, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()