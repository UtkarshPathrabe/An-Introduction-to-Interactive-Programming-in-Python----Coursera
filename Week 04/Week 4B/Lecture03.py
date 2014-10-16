###################################
# Lists (mutable) vs. tuples (immutable)

print [4, 5, 6]

print (4, 5, 6)

print type([4, 5, 6])

print type((4, 5, 6))

a = [4, 5, 6]
a[1] = 100
print a

b = (4, 5, 6)
b[1] = 100
print b
