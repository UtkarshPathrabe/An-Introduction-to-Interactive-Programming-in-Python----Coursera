Quiz
====

Question 1
----------

In the following code, what does the number `100` represent?  
`my_button = frame.add_button("My Label", button_handler, 100)`  

### Answer

Width of the button in pixels.  

Question 2
----------

How many control objects are allowed in a frame?  

### Answer

Unlimited, i.e., 0 or more  

Question 3
----------

In SimpleGUI, one kind of object can be added to the control panel that doesn't allow any handler. Thus, this object can't respond to anything. What kind of object is that?  

### Answer

Label  

Question 4
----------

When you enter text into an input field and press enter, the text is passed to the input field's event handler. What is the data type of the text?    

### Answer

A string  

### Explanation  

The entered data is a string. The text entered into an input field is always passed to the input handler as a string even if the text corresponds to a number.  

Question 5
----------

Consider the following conditional statement.  

if p == False:  
&nbsp;&nbsp;&nbsp;&nbsp;return False  
elif q == False:  
&nbsp;&nbsp;&nbsp;&nbsp;return False  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;return True  

That is equivalent to which of the following simpler statements?

### Answer

return q and p

Question 6
----------

Which of the following describes the mistake in the following code?  

def volume_cube(side):  
&nbsp;&nbsp;&nbsp;&nbsp;""" Returns the volume of a cube, given the length of its side. """  
&nbsp;&nbsp;&nbsp;&nbsp;print side ** 3  

s = 5  
print "The volume of a cube with sides", s, "long is", volume_cube(s), "."  

### Answer

The function should return, not print, its result.  

### Explanation

In most cases, functions should return their computed results. Furthermore, the documentation string here specifies that it should be returning that value.

Question 7
----------

What kind of errors can happen if you are missing a needed `global` declaration in one of your function definitions? For this question, you need only consider the case where the problem is in the function that is missing the `global` declaration.  

### Answer

An incorrect computation that generates no error message  

### Explanation

If you only assign to the variable, without trying to use its current value, you won't get any error message. Instead, Python assumes the variable is local, which might lead to an unexpected result.  

Question 8
----------

Which of the following function definitions are in the recommended code style?     

### Answer

def f(x, y):
&nbsp;&nbsp;&nbsp;&nbsp;""" Add the two inputs. """
&nbsp;&nbsp;&nbsp;&nbsp;return x + y  

### Explanation

1. def f (x, y):  
   &nbsp;&nbsp;&nbsp;&nbsp;""" Add the two inputs. """  
   &nbsp;&nbsp;&nbsp;&nbsp;return x + y  
   
   This does not follow recommended style, there shouldn't be a space before the parenthesis  
   
2. def myFunction(x, y):  
   &nbsp;&nbsp;&nbsp;&nbsp;""" Add the two inputs. """  
   &nbsp;&nbsp;&nbsp;&nbsp;return x + y  
   
   This does not follow recommended style, only class names should use "camel case".  
   
3. def f(x, y):  
   &nbsp;&nbsp;&nbsp;&nbsp;""" Add the two inputs. """  
   &nbsp;&nbsp;&nbsp;&nbsp;return x+y  
   
   This does not follow recommended style, there should be spaces around the addition operator.  

Question 9
----------

Cut and paste the following code into CodeSkulptor. Run it and make an attempt to understand how it works.  
We'd like to modify the code so that the count is reset to zero whenever a new message is entered. Where would you need to modify this code to implement this change?  

### Answer

Add an assignment to count in the event handler for the input field. Also add a global count declaration there.  

Question 10
-----------

In the game "Guess the number", what is the minimum number of guesses necessary to guarantee that the guesser can always win if the secret number is chosen in range(0, 400)?
Review the mini-project description for "Guess the number" if you are having trouble with this problem.  

### Answer

9 guesses

### Explanation

log to the base 2 (400) rounded to the higher side.  