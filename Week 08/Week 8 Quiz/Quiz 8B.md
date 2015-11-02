Quiz
====

Question 1
----------

Which of the following is valid notation for a set in [CodeSkulptor](http://www.codeskulptor.org/)?  

* `set([1, 2. 3])`  
* `set()`  
* `{}`  

### Answer

* `set([1, 2. 3])`  
* `set()`  

#### Explanation  

`{}` No, this is a dictionary.  

Question 2
----------

Which of the following operations can mutate set `s`? You may want to try some examples in CodeSkulptor and refer to the [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

* `s.difference_update(t)`  
* `t.difference(s)`  
* `s.update(s)`  
* `t.intersection_update(s)`  
* `s.pop()`  
* `s.difference(t)`  

### Answer  

* `s.difference_update(t)`  
* `s.pop()`  

#### Explanation  

While `s.update()` can change `s`, a set unioned with itself is just the same set.  

Question 3
----------

Which operation corresponds to the following description? Refer to the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  
Given two sets, `s` and `t`, we want a new set containing all the elements that are in one of the sets, but not both of the sets. For example, if `s` has the elements 1, 2, 3, 4, and `t` has the elements 3, 4, 5, 6, then the result should have the elements 1, 2, 5, 6.  

* `s.intersection(t)`  
* `s.difference(t)`  
* `s.symmetric_difference(t)`  
* `t.difference(s)`  

### Answer  

* `s.symmetric_difference(t)`  

Question 4
----------

A set is an unordered collection of distinct elements. Which of the following problem contexts represent instances of this idea?  

* Alphabetized names.  
* Names for everyone taking this course.  
* Group of distinct cities.  
* Rooms in a building.  

### Answer And Explanation   

* Alphabetized names.  
No, sets are not ordered.  
* Names for everyone taking this course.  
No, we could easily have multiple students with the same name.  
* Group of distinct cities.  
Yes, it can be represented as a set.  
* Rooms in a building.  
Yes, it can be represented as a set.  

Question 5
----------

How many frames per second are typically projected in modern movies? How many times per second is the draw handler typically called in CodeSkulptor?  
Enter two numbers representing these frame rates in frames per second. Use only spaces to separate the numbers.  

### Answer   

`24 60`  

Question 6
----------

The bonus portion of this week's mini-project defines and uses a `Sprite` class to support animations. Each animated sprite includes an associated tiled image, each of whose sub-images are drawn in turn during the process of animating the sprite.  
What attribute (also known as a field) of this `Sprite` class can be used to select the appropriate sub-image to draw during this animation process? (If you are stuck, review the bonus phase in the mini-project description.)  

* `sound`  
* `pos`  
* `angle_vel`  
* `angle`  
* `vel`  
* `animated`  
* `image_size`  
* `image`  
* `lifespan`  
* `image_center`  
* `radius`  
* `age`  

### Answer  

* `age`  

#### Explanation  

Here is the text of the relevant instruction from the bonus phase: "In the draw method of the Sprite class, check if `self.animated` is `True`. If so, then choose the correct tile in the image based on the age. The image is tiled horizontally. If `self.animated` is `False`, it should continue to draw the sprite as before."  

Question 7
----------

Consider a horizontally-tiled image where each sub-image has the same size. If each sub-image is of size 60×90 (in pixels), what is the horizontal distance (in pixels) between the centers of adjacent sub-images?  

* 180  
* 120  
* 90  
* 60  

### Answer  

* 60  

Question 8  
----------

How many <b>distinct</b> numbers are printed by the following code? Enter the count.  

```python
def next(x):
    return (x ** 2 + 79) % 997

x = 1
for i in range(1000):
    print x
    x = next(x)
```  
Hint: Consider how editing the code to use a set could help solve the question.  

### Answer  

`46`  

#### Explanation  

```python
def next(x):
    return (x ** 2 + 79) % 997

x = 1
Set = set([x])
for i in range(1000):
    x = next(x)
    Set.add(x)

print len(Set)

## 46
```  

Question 9  
----------  

Which instructor exhibits the best coding style?  

* Joe  
* Stephen  
* Scott  
* John  

### Answer  

* John  

#### Explanation  

John's programming tips are the best. We need to see more of him.  