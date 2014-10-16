Quiz
====

Question 1
----------

In Python, `[1, 2, 3]` is of type list. What is the name of the type of `(1, 2, 3)`?  

### Answer

Tuple    

Question 2
----------

Which of the following types of data are immutable in Python?  

### Answer

Numbers  
Strings  
Booleans  
Tuples    

Question 3
----------

Which of the following functions must include a `global point` declaration in order to change the global variable `point`?  
point = [0, 0]  
def function1():  
&nbsp;&nbsp;&nbsp;&nbsp;point[0] += 1  
&nbsp;&nbsp;&nbsp;&nbsp;point[1] += 2  
def function2():  
&nbsp;&nbsp;&nbsp;&nbsp;point = [50, 50]  

### Answer

function2  

### Explanation

See details in the python code file along with this document.  

Question 4
----------

Consider the following program.  
x = range(5)  
???  
???  
We can replace the question marks with what two statements to make both variables have the value `[0, 1, 10, 3, 4]`?    

### Answer

1. y = x  
&nbsp;&nbsp;&nbsp;&nbsp;x[2] = 10  
2. y = x  
&nbsp;&nbsp;&nbsp;&nbsp;y[-3] = 10  

### Explanation
  
See details in the python code file along with this document.  

Question 5
----------

In our program, the variable `position` represents a 2D position on the canvas. We want to be able to change the position by some amount in variable `delta`. Why is the following code snippet incorrect?  

position = [50, 50]  
delta = [1, -2]  
...  
position = position + delta  

Note that the ellipses represent that we might have code in between what is shown, but such code is irrelevant and omitted.  

### Answer

The `+` operator on lists does not mean addition of the numbers in a list.  

### Explanation

See details in the python code file along with this document.

Question 6
----------

Consider the following program.  

a = ["green", "blue", "white", "black"]  
b = a  
c = list(a)  
d = c  
a[3] = "red"  
c[2] = a[1]  
b = a[1 : 3]  
b[1] = c[2]  

At the end of this code, to how many list objects do the variables refer?  
If you run the code and print the variables' values, you can begin to answer this question. After all, if two variables print differently, they certainly can't refer to the same object. However, if two variables print the same, you still need to determine whether they refer to the same object. One way is to step through the code while drawing reference diagrams. Another is to mutate one and see if others also mutate.  

### Answer

3  

### Explanation

See details in the python code file along with this document. Run the corresponding code in Viz mode.

Question 7
----------

Convert the following specification into code. Do the point and rectangle ever overlap?  

A point starts at `[10, 20]`. It repeatedly changes position by `[3, 0.7]` - e.g., under button or timer control. Meanwhile, a rectangle stays in place. Its corners are at `[50, 50]` (upper left), `[180, 50]` (upper right), `[180, 140]` (lower right), and `[50, 140]` (lower left).    

To check for overlap, i.e., collision, just run your code and check visually. You do not need to implement a point-rectangle collision test. However, we encourage you to think about how you would implement such a test.  

### Answer

Yes  

### Explanation

See details in the python code file along with this document.  

Question 8
----------

Assume we are using acceleration control for a spaceship in a game. That is, we regularly have the following updates:  

* The position is incremented by the time interval multiplied by the velocity. This happens on each draw event.  
* The velocity is incremented by the time interval multiplied by the acceleration. This happens on each draw event.  
* The acceleration is periodically incremented by some fixed vector (the same vector for each step). This could happen on keyboard or timer events.  
Assume that, initially, the ship is stationary and subject to no acceleration. What sort of trajectory will the spaceship fly in?  

### Answer

Straight line

### Explanation

See details in the python code file along with this document.  
Since the change to acceleration is a fixed constant, the velocity will always be in the direction indicated by this constant.  

Question 9
-----------

Write a Python program that initializes a global variable to 5. The keydown event handler updates this global variable by doubling it, while the keyup event handler updates it by decrementing it by 3.  

What is the value of the global variable after 12 separate key presses, i.e., pressing and releasing one key at a time, and repeating this 12 times in total?  

To test your code, the global variable's value should be 35 after 4 key presses.    

### Answer

8195  

### Explanation

See details in the python code file along with this document.