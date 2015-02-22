# Question No 3
def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

print "--------------------------------------------------"

# Question No 4
n = 123
print (n % 100 - n % 10) / 10
print ((n - n % 10) / 10) % 10
print (n - n % 10) / 10

print "--------------------------------------------------"

# Question No 6
import math

def f(x):
    return (-5 * math.pow(x, 5)) + (69 * math.pow(x, 2)) - 47

print f(0)
print f(1)
print f(2)
print f(3)
print max(f(0), f(1), f(2), f(3))

print "--------------------------------------------------"

# Question No 7
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * math.pow(1 + rate_per_period, periods)

print "$500 at 4% compounded daily for 10 years yields $", future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print "--------------------------------------------------"

# Question No 8
def area_regular_polygon(no_of_sides, length_of_each_side):
    a = math.tan(math.pi / no_of_sides)
    b = (no_of_sides) * math.pow(length_of_each_side, 2)
    c = b / a
    return c / 4

print area_regular_polygon(5, 7)
print area_regular_polygon(7, 3)

print "--------------------------------------------------"

# Question No 9
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print "--------------------------------------------------"

# Question No 10
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
