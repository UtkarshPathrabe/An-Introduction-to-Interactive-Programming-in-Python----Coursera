Lecture 01 Quiz
===============  

Question
--------  
Which of the following statements will correctly create an object of type `Rice` and assign it to the variable `owls`? The `__init__` method of the class `Rice` takes two arguments: `self` and `greeting`.  

### Answer  
* `owls = Rice("hoot")`  

#### Explanation  
The class name (`Rice`) acts like a function to create objects of that type. You do not pass the first argument (`self`) to this function, as Python does that for you. The initializer (`__init__`) always returns the new object, which you can then assign to a variable.  