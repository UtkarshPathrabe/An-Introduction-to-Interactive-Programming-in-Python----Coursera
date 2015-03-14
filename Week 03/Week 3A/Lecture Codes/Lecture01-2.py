# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

import simplegui


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([100, 100], 50, 2, "Red", "Pink")
    canvas.draw_circle([300, 300], 50, 2, "Red", "Pink")
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100, 300], 50, 2, "Green", "Lime")
    canvas.draw_circle([300, 100], 50, 2, "Green", "Lime")
    canvas.draw_line([100, 300],[300, 100], 2, "Black")
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 
          "Blue", "Aqua")
    canvas.draw_text("An example of drawing", [60, 385], 24, "Black")

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")


# Start the frame animation
frame.start()
