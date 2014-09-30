# calculator with all buttons

import simplegui

# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(t):
    """ enter a new operand"""
    global operand
    operand = float(t)
    output()
    
# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers and create control elements
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Subtract", sub, 100)
f.add_button("Multiply", mult, 100)
f.add_button("Divide", div, 100)
f.add_input("Enter an Operand:", enter, 100)


# get frame rolling
f.start()