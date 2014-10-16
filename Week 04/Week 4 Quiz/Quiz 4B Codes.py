# Question 3
point = [0, 0]
def function1():
    point[0] += 1
    point[1] += 2
function1()
print point
def function2():
    point = [50, 50]
function2()
print point

# Question 4
x1 = range(5)
y1 = x1
x1 = [0, 1, 10, 3, 4]
print x1, y1
x2 = range(5)
y2 = x2
x2[2] = 10
print x2, y2
x3 = range(5)
y3 = x3
y3 = [0, 1, 10, 3, 4]
print x3, y3
x4 = range(5)
x4 = y4
x4[2] = 10
print x4, y4
x5 = range(5)
y5 = x5
y5[-3] = 10
print x5, y5
x6 = range(5)
y6[-3] = 10
x6 = y6
print x6, y6

# Question 5
position = [50, 50]
delta = [1, -2]
position = position + delta
print position

# Question 6 :- Run the code in viz mode
a = ["green", "blue", "white", "black"]
b = a
c = list(a)
d = c
a[3] = "red"
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]
print a
print b
print c
print d

# Question 7
import simplegui
# Initialize globals
WIDTH = 400
HEIGHT = 300
pos = [10, 20]
vel = [3, 0.7]
# define event handlers
def draw(canvas):
    # Update point position
    pos[0] += vel[0]
    pos[1] += vel[1]
    # Draw point
    canvas.draw_point(pos, 'White')
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], 1, 'Yellow', 'Orange')
# create frame
frame = simplegui.create_frame("Point physics", WIDTH, HEIGHT)
# register event handlers
frame.set_draw_handler(draw)
# start frame
frame.start()

# Question 8
import simplegui
# Initialize globals
WIDTH = 600
HEIGHT = 400
pos = [0, 0]
vel = [0.1, 0.07]
acc = [0, 0.01]
# define event handlers
def draw(canvas):
    # Update point position
    pos[0] += vel[0]
    pos[1] += vel[1]
    # Update point velocity
    vel[0] += acc[0]
    vel[1] += acc[1]
    # Draw ball
    canvas.draw_circle(pos, 10, 5, 'Yellow', 'Orange')
def key_handler(key):
    if key == simplegui.KEY_MAP["a"]:
        acc[0] += 0.01
        acc[1] += 0.02       
# create frame
frame = simplegui.create_frame("Point physics", WIDTH, HEIGHT)
# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
# start frame
frame.start()

# Question 9
import simplegui
# initialize state variables
count = 0
value = 5
# event handlers
def keydown(key):
    global count, value
    count += 1
    value *= 2
def keyup(key):
    global value
    value -= 3
def draw(c):
    c.draw_text(str(value), [10, 25], 20, "Red")
    c.draw_text(str(count), [100, 25], 20, "Yellow")
# create frame             
f = simplegui.create_frame("Output", 130, 35)
# register event handlers
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.set_draw_handler(draw)
# start frame
f.start()