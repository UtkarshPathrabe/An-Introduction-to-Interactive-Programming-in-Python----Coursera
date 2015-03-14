#####################
# Example of event-driven code, buggy version

import simplegui

size = 10
radius = 10

# Define event handlers.

def incr_button_handler():
    """Increment the size."""
    global size
    size += 1
    label.set_text("Value: " + str(size))
    
def decr_button_handler():
    """Decrement the size."""
    global size
    # Insert check that size > 1, to make sure it stays positive
    # NOTE that this restriction has changed from the video
    # since draw_circle now throws an error if radius is zero
    if size > 1:
        size -= 1
        label.set_text("Value: " + str(size))

def change_circle_handler():
    """Change the circle radius."""
    global radius
    radius = size
    # Insert code to make radius label change.
    radius_label.set_text("Radius: " + str(radius))
    
def draw_handler(canvas):
    """Draw the circle."""
    canvas.draw_circle((100, 100), radius, 5, "Red")

# Create a frame and assign callbacks to event handlers.

frame = simplegui.create_frame("Home", 200, 200)
label = frame.add_label("Value: " + str(size))
frame.add_button("Increase", incr_button_handler)
frame.add_button("Decrease", decr_button_handler)
radius_label = frame.add_label("Radius: " + str(radius))
frame.add_button("Change circle", change_circle_handler)
frame.set_draw_handler(draw_handler)

# Start the frame animation

frame.start()
