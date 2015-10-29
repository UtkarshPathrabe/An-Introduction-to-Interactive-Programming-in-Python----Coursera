Quiz
====

Question 1
----------

The class code provided for this week's mini-project supports an `ImageInfo` class to organize the data associated with the image. Consider an `ImageInfo` object of the following form:  
```python
ImageInfo([45, 45], [90, 90], 35)
```  
What is the radius of the shape associated with this `ImageInfo` object?  

### Answer

35  

#### Explanation  
This is the radius of the circle used in computing collisions involving the shape.  

Question 2
----------

Consider the provided `ImageInfo` and `Sprite` class code. Assume we want ten asteroids on the screen, each looking exactly alike and using the same image file. How many `ImageInfo` objects and how many `Sprite` objects should we create?  

* one `ImageInfo` object, one `Sprite` object  
* ten `ImageInfo` objects, one `Sprite` object  
* ten `ImageInfo` objects, ten `Sprite` objects  
* one `ImageInfo` object, ten `Sprite` objects  

### Answer  

* one `ImageInfo` object, ten `Sprite` objects  

#### Explanation  
Since there is one image file, there should be one `ImageInfo`. Since there are ten displayed asteroids, each potentially with its own velocity and angle, there should be ten `Sprite` objects.  

Question 3
----------

The version of <i>Rice Rocks</i> that we will implement uses only a single asteroid image and spawns multiple instances of the provided `Sprite` class using this image. In the original <i>Asteroids</i>, a large asteroid split into two medium asteroids which themselves split into two small asteroids.  
If we only had one image and wanted to implement asteroids of varying sizes in our version, how should we do this?  

* Add a size attribute in the `ImageInfo` class and a size parameter to `ImageInfo.__init__`. Use this attribute when drawing the sprite.  
* Store the size in a global variable. Use this variable when drawing a sprite.  
* Store a list of sizes for each asteroid in a global variable. Use the corresponding size when drawing a sprite.  
* Add a size attribute in the `Sprite` class and a size parameter to `Sprite.__init__`. Use the size attribute when drawing the sprite.  

### Answer  

* Add a size attribute in the `Sprite` class and a size parameter to `Sprite.__init__`. Use the size attribute when drawing the sprite.  

#### Explanation  
Adding a size attribute in the `Sprite` class allows each instance of a sprite to have a different size that can use in the draw method for the sprite.  

Question 4
----------

What is the supported range of sound volumes in `set_volume`? You can find out in the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

* 1 to 100  
* 0 to 1  
* 0 to 10  
* -1 to 1  

### Answer  

* 0 to 1  

Question 5
----------

Assume you have code that loads and plays a sound. Unfortunately, you don't hear anything. Which of the following could be a reason?  

### Answer   

* You have set the volume level to 0.  
* No file is found with the given URL.  
* A file found with the given URL isn't a sound file recognized by your browser.  
* The given URL exists, but is inaccessible due to network problems.  
* Your browser is loading a big sound file. Wait longer.  

Question 6
----------

Which of the following are valid HTML representations of the color blue?  
Refer to this page on [HTML color values]().  

* `"#FFFF00"`  
* `"#0000FF"`  
* `"blue"`  
* `"Red"`  
* `"rgb(0, 0, 255)"`  

### Answer  

* `"#0000FF"`  
* `"blue"`  
* `"rgb(0, 0, 255)"`  

Question 7
----------

Imagine we are writing code for something like Rice Rocks, where things are moving in 2D toroidal space, i.e., the wrap around all four sides of the screen. How can we eliminate the duplicated code in the following function?  
```python
def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    position[0] = (position[0] + vector[0]) % SCREEN_SIZE[0]
    position[1] = (position[1] + vector[1]) % SCREEN_SIZE[1]
```  

### Answer And Explanation  

```python
def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    position = (position + vector) % SCREEN_SIZE
```  
No, Invalid Python.  

```python
def move_dimension(dimension, position, vector):
    """Moves the position component by the given vector component in 1D toroidal space."""
    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]

def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    move_dimension(0, position, vector)
    move_dimension(1, position, vector)
```  
Yes, Valid Python Code.  

```python
def move(position, vector):
    position = [(pos + vec) % size for pos in position for vec in vector for size in SCREEN_SIZE]
```  
No, this doesn't have the same behavior.  

```python
NUM_DIMENSIONS = 2
def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    for d in range(NUM_DIMENSIONS):
        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]
```  
Yes, Valid Python Code.  

Question 8
----------

What is the primary reason for not duplicating code? It was the only reason mentioned in the Programming Tips #7 video.  

* You only need to get the code correct once.  
* It leads to faster code.  
* It takes less time to write the code.  

### Answer  

* You only need to get the code correct once.  

Question 9  
----------  

What is Mike Massimino's greatest accomplishment?  

* Appearing on An Introduction to Interactive Programming in Python.  
* Receiving his PhD from MIT.  
* Being the first person to use Twitter in space.  
* Appearing on The Big Bang Theory.  
* Fixing the Hubble Space Telescope in space.  

### Answer  

* Appearing on An Introduction to Interactive Programming in Python.  

#### Explanation  

Of course, how can you top this!  