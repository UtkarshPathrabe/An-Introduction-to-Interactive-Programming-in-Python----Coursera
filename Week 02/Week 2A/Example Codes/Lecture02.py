# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()


# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2


# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5.0 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)





# the risk/reward of using global variables

# risk - consider the software system for an airliner
#		critical piece - flight control system
#		non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!



# example
num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques