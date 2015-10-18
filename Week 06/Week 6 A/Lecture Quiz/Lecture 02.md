Lecture 02 Quiz
===============  

Question
--------  
What code would you need to write in order to extend the example of this lecture so that the ball would bounce around inside an oval?  

### Answer  
* You would need to write a class `OvalDomain` with the same methods as `RectangularDomain` and create an object of type `OvalDomain` to pass to the ball as its domain.  

#### Explanation  
Remember that one of the key benefits of object-oriented programming is that you can encapsulate behaviors. The ball doesn't need to know how the domain works. And the domain doesn't need to know how the ball works. So, you can write new domain types (or ball types) without having to change (or know about) any of the code in the other class' methods.  