Quiz
====

Question 1
----------

Let's define a class for 2-dimensional points.   
```python
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

    ...

```  
Which of the following code snippets are valid usages of the `Point2D` initializer and its `translate` method? For your first attempt at this problem, we suggest that you try to answer without using CodeSkulptor.  

### Answer And Explanation  

```python
point = Point2D(3, 9)
point.translate(5, -2)
```  
Yes, it is a valid code snippet.  

```python
point = Point2D(3, 9)
translate(point, 5, -2)
```  
No, `translate` is not defined globally. It is defined only for `Point2D` objects.  

```python
point1 = Point2D(3, 9)
point2 = Point2D()
point2.translate(20, 4)
```  
Yes, you can define multiple `Point2D` objects. Furthermore, the initializer is defined so that you don't have to provide arguments to `Point2D()`.  

```python
Point2D(3, 9)
Point2D.translate(5, -2)
```  
No, it is not a valid code snippet.  

Question 2
----------

Let's continue to use the same class for 2-dimensional points.  
```python
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

    ...

```  
Which of the following code snippets are valid usages of the `Point2D` initializer and its `translate` method? For your first attempt at this problem, we suggest that you try to answer without using CodeSkulptor.  

### Answer And Explanation  

```python
points = [(2, 5), (8, 3), (0, 2)]
for point in points:
    point.translate(-1, -1)
```  
No, `translate` is defined only on a `Point2D` object, not on a tuple.  

```python
point0 = Point2D(2, 5)
point1 = Point2D(8, 3)
point2 = Point2D(0, 2)
points = [point0, point1, point2]
points.translate(-1, -1)
```  
No, `translate` is defined only on a `Point2D` object, not on a list of `Point2D` objects.  

```python
points = [Point2D(2, 5), Point2D(8, 3), Point2D(0, 2)]
for point in points:
    point.translate(-1, -1)
```  
Yes, it is a valid code snippet.  

Question 3
----------

Let's continue to use the same class for 2-dimensional points.  
```python
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

    ...

```  
Which of the following code snippets are valid usages of the `Point2D` initializer and its `translate` method? For your first attempt at this problem, we suggest that you try to answer without using CodeSkulptor.  

```python
point = Point2D(3, 6)
lst = list(point)
```  

```python
point = Point2D(3, 6)
tup = tuple(point)
```  

```python
point = Point2D(3, 6)
s = str(point)
newpoint = Point(s)
```  

```python
point = Point2D(3, 6)
s = str(point)
```  

### Answer  

```python
point = Point2D(3, 6)
s = str(point)
```  

Question 4
----------

In SimpleGUI, the function `draw_image` takes an optional sixth parameter that determines the angle of rotation of the destination rectangle around its center. Do positive values for the angle rotate the image clockwise or counterclockwise? Is the angle specified in degrees or radians?  
Refer to the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

* clockwise, radians  
* counterclockwise, degrees  
* counterclockwise, radians
* clockwise, degrees  

### Answer  

* clockwise, radians  

Question 5
----------

One interesting extension of Rice Rocks would be to have two ships, with each controlled by a separate player, instead of one single ship. Using the provided class definitions, what is the best way to represent the two ships in this new variant?  

* Copy the `Ship` class code, e.g.,  
```python
class Another_Ship:
    def __init__(self, pos, vel, angle):
        ...
    ...
```  
Then create two ship objects, one of each class, assigning each to a global variable.  
```python
ship1 = Ship(...)
ship2 = Another_Ship(...)
```  

* Add another call to the `Ship` constructor, assigning the result to another global variable.  
```python
ship1 = Ship(...)
ship2 = Ship(...)
```  

* In the `Ship` class definition, change the variables `pos`, `vel`, `angle` to be lists of two values each. Then, change each method to take an additional number argument that indicates which ship should be used. Thus, when we call the constructor now, we are creating both ships.  
```python
ships = Ship(...)
```  

* In the `Ship` class definition, duplicate every method. For example, `Ship.draw1(...)` would be used to draw the first ship, while `Ship.draw2(...)` would be used to draw the second ship.  

### Answer  

* Add another call to the `Ship` constructor, assigning the result to another global variable.  
```python
ship1 = Ship(...)
ship2 = Ship(...)
```  

Question 6
----------

Which of the following browsers fully support MP3 audio files? Refer to the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

### Answer And Explanation  

* Firefox  
No, Firefox currently supports MP3 files on some, but not all systems.  
* Safari  
Yes, Safari fully supports MP3 audio files.  
* Chrome  
Yes, Chrome fully supports MP3 audio files.  

Question 7
----------

Consider a spaceship where the ship's thrusters can accelerate the ship by 10 pixels per second for each second that the thrust key is held down. If the friction induces a deceleration that is 10% of the ship's velocity per second, what is the maximal velocity of the ship? If you are having trouble, consider writing a short program to help understand this problem.  

* Around 1000 pixels per second.  
* Around 10 pixels per second.  
* The ship has no maximal velocity. It can reach any velocity the player desires if you hold the thrust key down long enough.  
* Around 100 pixels per second.  

### Answer  

* Around 100 pixels per second.  

#### Explanation  
At a velocity of 100 pixels per second, friction would induce a deceleration of 10 pixels per second. This deceleration would exactly cancel an acceleration of 10 pixels per second from the thrusters. We used "around" here since the true maximal velocity depends on the rate at which the frame is drawn.  