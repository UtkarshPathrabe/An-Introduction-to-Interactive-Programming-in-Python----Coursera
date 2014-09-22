a = True
b = False
c = True
d = False

print a
print b

print "-----------------------"

print not a
print a and b
print a or b

print "-----------------------"

print (a and b) or (c and (not d))

# Comparison Operators
# >
# <
# >=
# <=
# ==
# !=

a = 7 > 3
print a

x = 5
y = 5
b = x > y
print b

c = "Hello" == 'Hello'
print c

d = 20.6 <= 18.3
print d

print (a and b) or (c and (not d))