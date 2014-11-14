import random

# Question 2
my_list = [1, 2, 3, 4, 5]
#my_list.extend([10, 20])
#my_list.reverse()
#my_list + [10, 20]
my_list.append(10)
print my_list

# Question 3
fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop(0)
print fruit, fruits

# Question 4
print range(2, 15, 3)
print range(14, 1, -3)
print range(2, 15)*3

# Question 6
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result
print reverse_string("hello")

# Question 7
def random_point():
    return (random.randrange(100), random.randrange(100))
def starting_points(players):
    points = []
    for player in players:
        point = random_point()
        points.append(point)
    return points
print starting_points(['abhay', 'devashish', 'tina', 'walt'])

# Question 8
def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            return False
    return True
print is_ascending([2, 6, 9, 12, 400])
print is_ascending([4, 8, 2, 13])

# Question 9
list = [0, 1]
i = 40
while i > 0:
    list.append(list[-1]+list[-2])
    i -= 1
print list.pop()