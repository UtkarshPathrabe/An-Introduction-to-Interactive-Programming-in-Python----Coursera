# ball physics code for generic 2D domain
# the functions inside() and normal() encode the shape of the ennvironment

import simplegui
import random
import math

# Canvas size
width = 600
height = 400

# Ball traits
radius = 20
color = "White"

# math helper function
def dot(v, w):
    return v[0] * w[0] + v[1] * w[1]

class RectangularDomain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = 2

    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        in_width = ((radius + self.border) < center[0] < 
                    (self.width - self.border - radius))
        in_height = ((radius + self.border) < center[1] < 
                     (self.height - self.border - radius))
        return in_width and in_height

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        left_dist = center[0]
        right_dist = self.width - center[0]
        top_dist = center[1]
        bottom_dist = self.height - center[1]
        if left_dist < min(right_dist, top_dist, bottom_dist):
            return (1, 0)
        elif right_dist < min(left_dist, top_dist, bottom_dist):
            return (-1, 0)
        elif top_dist < min(bottom_dist, left_dist, right_dist):
            return (0, 1)
        else:
            return (0, -1)

    # return random location
    def random_pos(self, radius):
        x = random.randrange(radius, self.width - radius - self.border)
        y = random.randrange(radius, self.height - radius - self.border)
        return [x, y]

    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_polygon([[0, 0], [self.width, 0], 
                             [self.width, self.height], [0, self.height]],
                             self.border*2, "Red")
        
class CircularDomain:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.border = 2
        
    # return if bounding circle is inside the domain    
    def inside(self, center, radius):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return dr < (self.radius - radius - self.border)

    # return a unit normal to the domain boundary point nearest center
    def normal(self, center):
        dx = center[0] - self.center[0]
        dy = center[1] - self.center[1]
        dr = math.sqrt(dx ** 2 + dy ** 2)
        return [dx / dr, dy / dr]
    
    # return random location
    def random_pos(self, radius):
        r = random.random() * (self.radius - radius - self.border)
        theta = random.random() * 2 * math.pi
        x = r * math.cos(theta) + self.center[0]
        y = r * math.sin(theta) + self.center[1]
        return [x, y]
        
    # Draw boundary of domain
    def draw(self, canvas):
        canvas.draw_circle(self.center, self.radius, self.border*2, "Red")
    
class Ball:
    def __init__(self, radius, color, domain):
        self.radius = radius
        self.color = color
        self.domain = domain
        
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .1, random.random() + .1]
        
    # bounce
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
    

    # update ball position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()

    # draw
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, 
                           self.color, self.color)
        

# generic update code for ball physics
def draw(canvas):
    ball.update()
    field.draw(canvas)
    ball.draw(canvas)

field = RectangularDomain(width, height)
# field = CircularDomain([width/2, height/2], 180)
ball = Ball(radius, color, field)
        
frame = simplegui.create_frame("Ball physics", width, height)

frame.set_draw_handler(draw)

frame.start()