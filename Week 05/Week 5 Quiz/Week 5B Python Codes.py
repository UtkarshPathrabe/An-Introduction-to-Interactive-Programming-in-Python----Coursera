# Question 7
def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0
def even_numbers(my_list):
    return [n for n in my_list if is_even(n)]
print even_numbers([1, 3, 4, 5, 8, 9, 10, 11, 13, 12, 78])

# Question 9
import simplegui
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")
frame_size = [300, 300]
image_size = [380, 287]
def draw(canvas):
    canvas.draw_image(image,  [220, 100], [100, 100],
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)
frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
frame.start()