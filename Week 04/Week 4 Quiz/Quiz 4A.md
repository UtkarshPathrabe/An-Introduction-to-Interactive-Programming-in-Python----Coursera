Quiz
====

Question 1
----------

What built-in function will add all the numbers in a list of numbers? Just give the function name, without any parentheses or argument.  

### Answer

sum  

### Explanation

See details in the python code file along with this document.  

Question 2
----------

Let `my_list` be the list `["This", "course", "is", "great"]`.

What is `len(my_list)`?
What non-negative number is the index of `"great"`? I.e., how would you replace the question marks in `my_list[???]` so that the result is `"great"`?
Submit two numbers, one for each of these two questions, separated by spaces.  

### Answer

4 3  

### Explanation

See details in the python code file along with this document.  

Question 3
----------

Let `my_list` be the list `["This", "course", "is", "great"]`.

We can use Python's slice notation to get part of this list. What non-negative numbers can be used to get the slice `["course", "is"]`? I.e., what two non-negative numbers should we put in `my_list[??? : ???]` to get that result?

Submit the two numbers in order, separated only by spaces.  

### Answer

1 3  

### Explanation

See details in the python code file along with this document.  

Question 4
----------

If we want to split a list `my_list` into two halves, which of the following uses slices to do so correctly?

More precisely, if the length of `my_list` is 2n, i.e., even, then the two parts should each have length n. If its length is 2n+1, i.e., odd, then the two parts should have lengths n and n+1.  

### Answer

`my_list[0 : len(my_list) // 2]` and `my_list[len(my_list) // 2 : len(my_list)]`  
`my_list[: len(my_list) // 2]` and `my_list[len(my_list) // 2 :]`  

### Explanation

`my_list[0 : len(my_list) // 2]` and `my_list[len(my_list) // 2 + 1 : len(my_list)]`  
&nbsp;&nbsp;&nbsp;&nbsp;:The list element at index `len(my_list) // 2` is not in either part.  
`my_list[: len(my_list) // 2 - 1]` and `my_list[len(my_list) // 2 :]`  
&nbsp;&nbsp;&nbsp;&nbsp;:The list element at index `len(my_list) // 2 - 1` is not in either part.  
See details in the python code file along with this document.  

Question 5
----------

What is the distance between point `[4, 7]` and the nearest point on the circle centered at `[2, 9]` with radius 2? Provide at least 4 digits of accuracy.

Hint: The distance between a point and a circle is the distance between the point and the center of the circle minus the radius of the circle. You can use the point-to-point distance code described in this week's videos.  

### Answer

0.82842712475  

### Explanation

See details in the python code file along with this document.

Question 6
----------

A ball with velocity `[4, 2]` reflects off a vertical wall. What is its new velocity?  

### Answer

`[-4, 2]`  

### Explanation

On collision with a vertical wall only the X component of velocity changes, i.e. it becomes negative.

Question 7
----------

Which of the following illustrate how to properly structure a keydown or keyup event handler? (For more advanced Python programmers, assume that you have just imported simplegui and haven't used `from`.)  

### Answer

def keydown_handler(key):  
&nbsp;&nbsp;&nbsp;&nbsp;if key == simplegui.KEY_MAP["left"]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...    

Question 8
----------

Assume you have a program with a keydown handler. You run it, and press a single key and hold it down continuously. How many times does the keydown handler get called?  

### Answer

1  

Question 9
-----------

Several keys on the keyboard, such as Shift, CapsLock, and Ctrl, typically act to modify what happens when you press other keys, rather than doing anything on their own. When using the SimpleGUI keydown handler, how are such keys treated?  

### Answer

Independent key press events - e.g., pressing Shift by itself creates an event.  

### Explanation

Yes, for example Shift gives the value 16, Control key gives the value of 17 etc.