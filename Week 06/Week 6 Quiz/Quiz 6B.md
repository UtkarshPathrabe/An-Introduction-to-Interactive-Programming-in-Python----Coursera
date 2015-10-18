Quiz
====

Question 1
----------

What is the position of the center of the top-left card (Ace of Clubs) in the [tiled image](http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png) discussed in the "Tiled images" video? Remember that each card in this tiled image has size 73 x 98 pixels.  
(Note that the tiled image used in the current version of your Blackjack mini-project is slightly smaller.)  

* `(5 * 73 + 36.5, 1 * 98 + 49)`  
* `(73, 98)`  
* `(36.5, 49)`  
* `(0, 0)`  

### Answer

* `(36.5, 49)`  

#### Explanation  
Divide each dimension of card size by 2.  

Question 2
----------

What is the position of the center of the bottom-right card (King of Diamonds) in the [tiled image](http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png) discussed in the "Tiled images" video? Again, remember that each card in this tiled image has size 73 x 98 pixels.  
Enter two numbers, separated only by spaces.  

### Answer  

912.5 343  

#### Explanation  
i = 36.5 + (73 * 12)  
j = 49 + (98 * 3)  

Question 3
----------

When using Dropbox to store images for use with CodeSkulptor, what should the `www` portion of the DropBox URL be replaced by?  
Refer to the video on tiled images.  

* `dl`  
* `www`  
* `gif`  
* `html`  
* `jpg`  

### Answer  

* `dl`  

#### Explanation  
`dl` specifies that the file is for download.  

Question 4
----------

Within the `__init__` method, the new object should be returned with what code?  

* No `return` statement is needed in `__init__`.  
* `return self`  
* `return whatever_the_object_is_named` (Use the appropriate variable name.)  
* `return`  

### Answer  

* No `return` statement is needed in `__init__`.  

#### Explanation  
Here are some hidden details to explain this potentially confusing behavior. Each Python class has a hidden constructor method that  

* Constructs (makes) the object.  
* Calls `__init__` to initialize the object,
* Then returns this object.  

So, while there is a `return` statement somewhere, it is in this hidden constructor method that you don't have to define.  

Question 5
----------

One way of understanding code is to think about other code that accomplishes the same thing - i.e., given the same starting values, it returns and/or mutates the same values.  
This following defines one way to concatenate multiple lists. For example, `list_extend_many([[1,2], [3], [4, 5, 6], [7]])` returns `[1, 2, 3, 4, 5, 6, 7]` and doesn't mutate anything.  
```python
def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result
```  
Which of the following definitions are equivalent? I.e., which always produce the same output for the same input, and never mutate the input or any global variable?  

### Answer And Explanation   

```python
def list_extend_many(lists):
    result = []
    while len(lists) > 0:
        result.extend(lists.pop(0))
    return result
```  
Not the answer. This returns the correct result, but it mutates the argument in the process, making it empty!  

```python
def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists): 
        result.extend(lists[i])
        i += 1
    return result
```  
Correct Answer.  

```python
def list_extend_many(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result
```  
Correct Answer. We can also loop over indices.  

```python
def list_extend_many(lists):
    result = []
    i = 0
    while i <= len(lists): 
        result.extend(lists[i])
        i += 1
    return result
```  
Not the answer. This loops one too many times.  

Question 6
----------

Which of the following programs would never end if it weren't for CodeSkulptor's timeout? Assume no `break` or `return` statement is used in the elided loop bodies.  
You might want to add a `print` statement to each loop to better understand the behavior.  

### Answer  

```python
n = 1000
while n > 0:
    ...     # Assume this doesn't modify n.
    n -= 1
```  
Not the answer. This loop would eventually terminate.  

```python
my_list = .
for x in my_list:
    ...     # Assume this doesn't mutate my_list.
```  
Not the answer. This loop would eventually terminate.  

```python
n = 1001
while n != 0:
    ...     # Assume this doesn't modify n.
    n -= 2
```  
Correct Answer. `n` would never reach zero in the loop and hence the loop would go on till infinity or `TIME_LIMIT_EXCEEDED` Error would be raised.  

```python
n = 127834876
while n >= 0:
    ...     # Assume this doesn't modify n.
    n //= 2
```  
Correct Answer. `n` would eventually reach zero but then would never change in the loop and hence the loop would go on till infinity or `TIME_LIMIT_EXCEEDED` Error would be raised.  

Question 7
----------

Convert the following English description into code.  

1. Initialize `n` to be 1000. Initialize `numbers` to be a list of numbers from 2 to n, but not including `n`.  
2. With `results` starting as the empty list, repeat the following as long as `numbers` contains any numbers.  
    * Add the first number in `numbers` to the end of results.  
    * Remove every number in `numbers` that is evenly divisible by (has no remainder when divided by) the number that you had just added to `results`.  

How long is `results`?  
To test your code, when `n` is instead 100, the length of `results` is 25.

### Answer  

168  

#### Explanation  
This computes the primes less than n by a process known as the Sieve of Eratosthenes.  
By the way, here's one way to write this:  
```python
n = 1000
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]

print len(results)

## 168
```  

Question 8
----------

We can use loops to simulate natural processes over time. Write a program that calculates the populations of two kinds of "wumpuses" over time. At the beginning of year 1, there are 1000 slow wumpuses and 1 fast wumpus. This one fast wumpus is a new mutation. Not surprisingly, being fast gives it an advantage, as it can better escape from predators. Each year, each wumpus has one offspring. (We'll ignore the more realistic niceties of sexual reproduction, like distinguishing males and females.). There are no further mutations, so slow wumpuses beget slow wumpuses, and fast wumpuses beget fast wumpuses. Also, each year 40% of all slow wumpuses die each year, while only 30% of the fast wumpuses do.  
So, at the beginning of year one there are 1000 slow wumpuses. Another 1000 slow wumpuses are born. But, 40% of these 2000 slow wumpuses die, leaving a total of 1200 at the end of year one. Meanwhile, in the same year, we begin with 1 fast wumpus, 1 more is born, and 30% of these die, leaving 1.4. (We'll also allow fractional populations, for simplicity.)  
Enter the first year in which the fast wumpuses outnumber the slow wumpuses. Remember that the table above shows the populations at the start of the year.  

### Answer  

45  

#### Explanation  
```python
year = 1
numberOfSlowWumpuses = 1000
numberOfFastWumpuses = 1
print year, numberOfSlowWumpuses, numberOfFastWumpuses
while numberOfSlowWumpuses >= numberOfFastWumpuses:
    numberOfSlowWumpuses *= 2
    numberOfSlowWumpuses *= 0.6
    numberOfFastWumpuses *= 2
    numberOfFastWumpuses *= 0.7
    year += 1
    print year, numberOfSlowWumpuses, numberOfFastWumpuses

## 1 1000 1
## 2 1200.0 1.4
## 3 1440.0 1.96
## 4 1728.0 2.744
## 5 2073.6 3.8416
## 6 2488.32 5.37824
## 7 2985.984 7.529536
## 8 3583.1808 10.5413504
## 9 4299.81696 14.75789056
## 10 5159.780352 20.661046784
## 11 6191.7364224 28.9254654976
## 12 7430.08370688 40.4956516966
## 13 8916.10044826 56.6939123753
## 14 10699.3205379 79.3714773254
## 15 12839.1846455 111.120068256
## 16 15407.0215746 155.568095558
## 17 18488.4258895 217.795333781
## 18 22186.1110674 304.913467293
## 19 26623.3332809 426.878854211
## 20 31947.9999371 597.630395895
## 21 38337.5999245 836.682554253
## 22 46005.1199094 1171.35557595
## 23 55206.1438912 1639.89780634
## 24 66247.3726695 2295.85692887
## 25 79496.8472034 3214.19970042
## 26 95396.2166441 4499.87958058
## 27 114475.459973 6299.83141282
## 28 137370.551967 8819.76397795
## 29 164844.662361 12347.6695691
## 30 197813.594833 17286.7373968
## 31 237376.3138 24201.4323555
## 32 284851.57656 33882.0052977
## 33 341821.891872 47434.8074167
## 34 410186.270246 66408.7303834
## 35 492223.524295 92972.2225368
## 36 590668.229154 130161.111552
## 37 708801.874985 182225.556172
## 38 850562.249982 255115.778641
## 39 1020674.69998 357162.090097
## 40 1224809.63997 500026.926136
## 41 1469771.56797 700037.696591
## 42 1763725.88156 980052.775227
## 43 2116471.05788 1372073.88532
## 44 2539765.26945 1920903.43945
## 45 3047718.32334 2689264.81522
## 46 3657261.98801 3764970.74131
```  
The answer is 45 because these are the populations at the beginning of the given year. So, at the beginning of the 46th year, i.e. at the end of 45th year the fast wumpuses outnumber the slow wumpuses.  