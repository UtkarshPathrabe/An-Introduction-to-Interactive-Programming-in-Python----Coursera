Quiz
====

Question 1
----------

Which of the following expressions corresponds to a dictionary with no elements?  

* `{}`  
* `None`  
* `()`  
* `dict()`  
* `[]`  

### Answer

* `{}`  
* `dict()`  

Question 2
----------

Given an existing dictionary `favorites`, what Python statement adds the key `"fruit"` to this dictionary with the corresponding value `"blackberry"`?  

* `favorites["fruit" = "blackberry"]`  
* `favorites{"fruit" : "blackberry"}`  
* `favorites["fruit"] = "blackberry"`  
* `favorites = {"fruit" : "blackberry"}`  

### Answer  

* `favorites["fruit"] = "blackberry"`  

#### Explanation

```python
favorites = {"fruit" : "blackberry"}  
```  
This statement creates a new dictionary instead of adding to an existing dictionary.  

Question 3
----------

Keys in a dictionary can have which of the following types?  

* Numbers  
* Dictionaries  
* Tuples  
* Lists  
* Strings  

### Answer  

* Numbers  
* Tuples  
* Strings  

#### Explanation  
Keys in a dictionary can have any immutable data type.  

Question 4
----------

Values in a dictionary can have which of the following types?    

* Dictionaries  
* Tuples  
* Lists  
* Numbers  

### Answer  

* Dictionaries  
* Tuples  
* Lists  
* Numbers  

#### Explanation  
Values in a dictionary can be of any data type.  

Question 5
----------

We often want to loop over all the key/value pairs in a dictionary. Assume the variable `my_dict` stores a dictionary. One way of looping like this is as follows:  

```python
for key in my_dict:
    value = my_dict[key]
    ...
```  
However, there is a better way. We can instead write the following:  
```python
for key, value in ???:
    ...
```  
What code should replace the question marks so that the two forms are equivalent? Refer to the video on dictionaries or the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).

* `items(my_dict)`  
* `my_dict.keys()`  
* `list(my_dict)`  
* `my_dict.values()`  
* `my_dict.keys_values()`  
* `my_dict.items()`  

### Answer  

* `my_dict.items()`  

Question 6
----------

Conceptually, the purpose of a dictionary is to represent a relationship between two collections of data - each key in the dictionary is related to one value. Which of the following situations are instances of such a relationship?  
Do not include situations where you have to introduce additional information in order to fit them into such a relationship.  

### Answer and Explanation   

* Storing names and IDs (identification numbers).  
Yes, map each ID (key) to the corresponding name (value). Each ID should be unique - otherwise it shouldn't be considered an ID.  
* Storing `x` and `y` coordinates of an arbitrary collection of 2-dimensional points.  
Not in general. This would make sense if the points were for a function, so that each x coordinate occurred at most once.  
* Storing where each person lives.  
Yes, map each person (key) to the corresponding address (value).  
* Computing averages.  
No, dictionaries don't compute anything.  

Note that it is possible to use dictionaries to represent sets and ordered collections. However, the focus of this question is on the relationship between data.  

Question 7
----------

Assume we have the following definition:  
```python
def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0
```  
Which of the following will compute a list of all of the even elements of list `my_list`?  
Refer to this week's Programming Tips video about list comprehensions. Also, try each example in [CodeSkulptor](http://www.codeskulptor.org/) before answering the question.

* `[n for n in my_list if is_even(n)]`  
* `[number for number in my_list if is_even(number)]`  
* `[is_even(number) for number in my_list]`  
* `[if is_even(number): number for number in my_list]`  

### Answer  

* `[n for n in my_list if is_even(n)]`  
* `[number for number in my_list if is_even(number)]`  

#### Explanation  
* `[is_even(number) for number in my_list]`  
Returns a list of Booleans.  
* `[if is_even(number): number for number in my_list]`  
Syntactically incorrect.  

Question 8
----------

You have the following code. The goal is to display a portion of the image, rescaling it to fill the canvas.  

```python
import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image, image_size, [image_size[0] / 2, image_size[1] / 2], [frame_size[0] / 2, frame_size[1] / 2], frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

frame.start()
```  
Run it, and observe that nothing is displayed in the frame. What is the problem?  

* The file doesn't exist.  
* The file is not an image.  
* The source arguments in `draw_image` are incorrect. We are trying to load pixels that are not within the image, and thus the draw fails.  
* The destination arguments in `draw_image` are incorrect. We aren't specifying values that would draw the image on this size canvas.  
* One or more of the `draw_image` arguments are of the wrong type.  

### Answer  

* The source arguments in `draw_image` are incorrect. We are trying to load pixels that are not within the image, and thus the draw fails.  

Question 9
----------

Write a CodeSkulptor program that loads and draws the following image:  
[http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png](http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png) with a source center of [220, 100] and a source size of [100, 100]. What one word appears in the canvas? If a letter is capitalized in the image, enter it as a capital.  
Note that you do have to position the image as stated to see the correct word.  

### Answer  

`tin`  

#### Explanation  

```python
import simplegui
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")
frame_size = [300, 300]
image_size = [380, 287]
def draw(canvas):
    canvas.draw_image(image,  [220, 100], [100, 100], [frame_size[0] / 2, frame_size[1] / 2], frame_size)
frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
frame.start()
```