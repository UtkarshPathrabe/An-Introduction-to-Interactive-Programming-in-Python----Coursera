Quiz
====

Question 1
----------

What is the type of the parameter for a mouseclick handler?  
Refer to the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

* String.  
* List.  
* Tuple.  
* Boolean.  
* Number.  
* There is no parameter.  

### Answer

* Tuple  

Question 2
----------

Which of the following expressions mutate, i.e., change, list `my_list`? If you've forgotten what the operations do, you can look in the CodeSkulptor [documentation](http://www.codeskulptor.org/docs.html#tabs-Python).  

* `my_list.extend([10, 20])`  
* `another_list.extend(my_list)`  
* `my_list + [10, 20]`  
* `my_list.append(10)`  
* `my_list.reverse()`  

### Answer  

* `my_list.extend([10, 20])`
* `my_list.append(10)`  
* `my_list.reverse()`  

#### Explanation

```python
my_list = [100, 200, 300]

my_list.extend([10, 20])
print my_list
# [100, 200, 300, 10, 20]

my_list + [10, 20]
print my_list
# [100, 200, 300]

my_list.append(10)
print my_list
# [100, 200, 300, 10]

my_list.reverse()
print my_list
# [300, 200, 100]
```  

Question 3
----------

We want to remove the element at the front of a list. For example, we want the following code to print `"apple"` and `["pear", "blueberry"]`, respectively. What function or method call should replace the question marks?  

```python
fruits = ["apple", "pear", "blueberry"]
fruit = ???
print fruit, fruits
```  

* `fruits.pop()`  
* `fruits.remove(0)`  
* `fruits.remove("apple")`  
* `fruits[0]`  
* `fruits[1:]`
* `fruits.pop(0)`  

### Answer  

* `fruits.pop(0)`  

#### Explanation  
```python
fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop(0)
print fruit, fruits
# apple ['pear', 'blueberry']
```  

Question 4
----------

Which of the following uses of `range()` will generate the list `[2, 5, 8, 11, 14]`?  
First, think about what each of these returns, but also try each in [CodeSkulptor](http://www.codeskulptor.org/docs.html#tabs-Python).    

* `range(2, 15) * 3`  
* `range(2, 14, 3)`  
* `range(2, 15, 3)`  

### Answer  

* `fruits.pop(0)`  

#### Explanation  
```python
print range(2, 15) * 3
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print range(2, 14, 3)
# [2, 5, 8, 11]

print range(2, 15, 3)
# [2, 5, 8, 11, 14]
```  

Question 5
----------

To correctly compute the product of a list `numbers` of numbers, what statement should replace the question marks?  

```python
numbers = .
???
for n in numbers:
    product *= n
```  

* `product = numbers[1]`  
* `product = []`  
* `product = 1`  
* `product = 0`  
* `product = numbers[0]`  

### Answer  

* `product = 1`  

Question 6
----------

We can loop over strings, too!  
The following incomplete function is a simple, but inefficient, way to reverse a string. What line of code needs to replace the questions marks for the code to work correctly?  

```python
def reverse_string(s):
    """Returns the reversal of the given string."""
    ???
    for char in s:
        result = char + result
    return result

print reverse_string("hello")
```  

* `result = " "`  
* `result = 0`  
* `result = []`  
* `result = ""`    

### Answer  

* `result = ""`  

Question 7
----------

Imagine a game on a map. At the beginning, we might want to randomly assign each player a starting point. Which of the following expressions may we use in place of the question marks to correctly implement this functionality?  

```python
import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        ???
    return points
```  

* `points.append(point)`  
* `points.extend(point)`  
* `point.append(points)`  
* `point.extend(points)`  
* `points + point`  
* `points += point`  

### Answer  

* `points.append(point)`  

Question 8
----------

The following function is supposed to check whether the given list of numbers is in ascending order. For example, we want `is_ascending([2, 6, 9, 12, 400])` to return `True`, while `is_ascending([4, 8, 2, 13])` should return `False`.  

```python
def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers)):
        if numbers[i+1] < numbers[i]:
            return False
    return True
```  
However, the function doesn't quite work. Try it on the suggested tests to verify this for yourself. The easiest fix is to make a small change to the highlighted code. What should it be replaced with?  

* `range(len(numbers - 1))`  
* `range(len(numbers)) - 1`  
* `range(len(numbers) - 1)`  
* `range(1, len(numbers))`  

### Answer  

* `range(len(numbers) - 1)`  

Question 9
----------

Turn the following English description into code:  

1. Create a list with two numbers, 0 and 1, respectively.  
2. For 40 times, add to the end of the list the sum of the last two numbers.  

What is the last number in the list?  
To test your code, if you repeat 10 times, rather than 40, your answer should be 89.  

### Answer  

165580141

#### Explanation  

```python
list = [0, 1]
i = 40
while i > 0:
    list.append(list[-1] + list[-2])
    i -= 1
print list.pop()  
```