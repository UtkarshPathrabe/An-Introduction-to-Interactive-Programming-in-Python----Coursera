Lecture 03 Quiz
===============  

Question
--------  
If particle is a Python list, what will happen if you execute the following line of Python in the draw handler:  
`particle.draw(canvas)`  

### Answer  
* You will get an AttributeError because list does not have a draw method.  

#### Explanation  
Remember that if you try to call a method and get an AttributeError you should check the type of the object (using type()) to make sure it is the type of object you think it is. Unfortunately, Python cannot read your mind and convert objects from one type to the type you want them to have.  