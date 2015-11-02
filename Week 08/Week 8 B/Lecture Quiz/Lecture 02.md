Lecture 02 Quiz
===============  

Question
--------  
What does the following code print?  

```python
s = set([1, 2, 3])
t = set([2, 3, 4])
r = s
s.intersection_update(t)
q = s.union(r)
print q
```  

### Answer  
* `set([2, 3])`  

#### Explanation  
Remember that r = s results in r and s referring to the same set. Also, remember that intersection_update mutates the set and union leaves the set unchanged while returning a new set.  