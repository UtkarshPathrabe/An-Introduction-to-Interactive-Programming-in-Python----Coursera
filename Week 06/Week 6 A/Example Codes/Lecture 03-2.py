# Testing template for Particle class


###################################################
# Student should add code for the Particle class here
    


###################################################
# Test code for the Particle class


p = Particle([20, 20], "Red")
print p
print type(p)
p.move([10, 20])
print p
p.move([-15, -25])
print p
print
q = Particle([15, 30], "Green")
print q
print type(q)
q.move([0, 0])
print q


###################################################
# Output from test

#Particle with position = [20, 20] and color = Red
#<class '__main__.Particle'>
#Particle with position = [30, 40] and color = Red
#Particle with position = [15, 15] and color = Red
#
#Particle with position = [15, 30] and color = Green
#<class '__main__.Particle'>
#Particle with position = [15, 30] and color = Green
