##################
# Object creation and use
# Mutation with Aliasing

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, newx):
        self.x = newx
    
    def get_x(self):
        return self.x

p = Point1(4, 5)
q = Point1(4, 5)
r = p

p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()


##################
# Object shared state
# Mutation of shared state

class Point2:
    def __init__(self, coordinates):
        self.coords = coordinates
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point2(coordinates)
q = Point2(coordinates)
r = Point2([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)


##################
# Objects not sharing state

class Point3:
    def __init__(self, coordinates):
        self.coords = list(coordinates)
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]
p = Point3(coordinates)
q = Point3(coordinates)
r = Point3([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)