# variables - placeholders for important values
# used to avoid recomputing values and to
# give values names that help reader understand code


# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja



# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Joe Warren"
print my_name

my_age = 51
print my_age

# birthday - add one

#my_age += 1
print my_age


# the story of the magic pill

magic_pill = 30
print my_age - magic_pill

my_grand_dad = 74

print my_grand_dad - 2 * magic_pill









# Temperature examples

# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

temp_Fahrenheit = 212

temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)

print temp_Celsius

# test it! 32 Fahrenheit is 0 Celsius, 212 Fahrenheit is 100 Celsius


# convert from Celsius to Fahrenheit
# f = 9 / 5 * c + 32

temp_Celsius = 100

temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32

print temp_Fahrenheit


# test it!
