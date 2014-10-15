import math

# Question 1
list1 = [0, 1, 2, 3, 4, 5]
print sum(list1)

# Question 2, 3, 4
my_list = ["This", "course", "is", "great"]
print len(my_list)
print my_list[3]
print my_list[1:3]
print my_list[0 : len(my_list) // 2]
print my_list[len(my_list) // 2 : len(my_list)]
print my_list[: len(my_list) // 2]
print my_list[len(my_list) // 2 :]

# Question 5
point1 = [4, 7]
point2 = [2, 9]
distance = math.sqrt(((point2[0]-point1[0])**2) + ((point2[1]-point1[1])**2))
print distance