##############
# Example of missing "global"

n1 = 0

def increment():
    n1 = n1 + 1

increment()
increment()
increment()

print n1


##############
# Example of missing "global"

n2 = 0

def assign(x):
    n2 = x

assign(2)
assign(15)
assign(7)

print n2


##############
# Example of missing "return"

n3 = 0

def decrement():
    global n3
    n3 = n3 - 1

x = decrement()

print "x = ", x
print "n = ", n


##############
# Example of print debugging

import simplegui

x = 0

def f(n):
    print "f: n,x = ", n, x
    result = n ** x
    print "f: result = ",result
    return result
    
def button_handler():
    global x
    print "bh : x = ", x
    x += 1
    print "bh : x = ", x

def input_handler(text):
    print "ih : text = ", text
    print f(float(text))
    
frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler, 100)

frame.start()


##############
# Examples of simplifying conditionals

def f1(a, b):
    """Returns True exactly when a is False and b is True."""  
    if a == False and b == True:
        return True
    else:
        return False

def f2(a, b):
    """Returns True exactly when a is False and b is True."""  
    if not a and b:
        return True
    else:
        return False    

def f3(a, b):
    """Returns True exactly when a is False and b is True."""  
    return not a and b

def g1(a, b):
    """Returns False eactly when a and b are both True."""  
    if a == True and b == True:
        return False
    else:
        return True
    
def g2(a, b):
    """Returns False eactly when a and b are both True."""  
    if a and b:
        return False
    else:
        return True

def g3(a, b):
    """Returns False eactly when a and b are both True."""  
    return not (a and b)
