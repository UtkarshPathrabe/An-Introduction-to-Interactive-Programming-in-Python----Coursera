Quiz
====
        
Question 1
----------
        
What does this program print?  

a = 42  
def f():  
&nbsp;&nbsp;&nbsp;&nbsp;a = 27  
&nbsp;&nbsp;&nbsp;&nbsp;return a  
b = f()  
print a  

### Answer

42  

### Explanation

The variable a is not declared global in f, so it does not affect the global a.  

Question 2
----------

What does this program print?  

def f(x):  
&nbsp;&nbsp;&nbsp;&nbsp;y = x + 3  
y = f(4)  
print y  

### Answer

None  

### Explanation

There is no return statement, so f returns None.  

Question 3
----------

Which expressions are the same as:  

a or b and c  

### Answer

a or (b and c)  
b and c or a  