###################
# Broken code

class ball:
    def ball(pos, rad):
        position = pos
        radius = rad
        return ball
    
    def get_position():
        return position

b = ball([0,0], 10)

print get_position(b)



###################
# Fixed code

class Ball:
    def __init__(self, pos, rad):
        self.position = pos
        self.radius = rad
    
    def get_position(self):
        return self.position

b = Ball([0,0], 10)

print b.get_position()


##################
# Example while

def countdown(n):
    """Print the values from n to 0."""

    i = n
    while i >= 0:
        print i
        i -= 1

countdown(5)


##################
# Collatz

def collatz(n):
    """Prints the values in the Collatz sequence for n."""

    i = n
    while i > 1:
        print i
        
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
           
colnatz(1000)


#################
# Timeout

i = 1
while i > 0:
    i += 1
	
print "Done!"
