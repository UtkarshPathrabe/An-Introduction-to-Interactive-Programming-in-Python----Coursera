###################################
# Mutation vs. assignment


################
# Look alike, but different

a = [4, 5, 6]
b = [4, 5, 6]
print "Original a and b:", a, b
print "Are they same thing?", a is b

a[1] = 20
print "New a and b:", a, b
print

################
# Aliased

c = [4, 5, 6]
d = c
print "Original c and d:", c, d
print "Are they same thing?", c is d

c[1] = 20
print "New c and d:", c, d
print

################
# Copied

e = [4, 5, 6]
f = list(e)
print "Original e and f:", e, f
print "Are they same thing?", e is f

e[1] = 20
print "New e and f:", e, f
print


###################################
# Interaction with globals


a = [4, 5, 6]

def mutate_part(x):
    a[1] = x

def assign_whole(x):
    a = x

def assign_whole_global(x):
    global a
    a = x

mutate_part(100)
print a

assign_whole(200)
print a

assign_whole_global(300)
print a