# First python program
print("Welcome to python!")

# Variables - Variables are containers for storing data values.
current_age = 20  # int
print(current_age)
print("1st way Age :- ", current_age)

strAge = str(current_age)  # string
print("2nd way Age :- " + strAge)

first_name = "John"  # string
lastName = "Doe"  # string
# + concatenation
full_name = first_name + " " + lastName
print("Name of the person is " + full_name)

is_online = False
print("Value of  is_online " + str(is_online))
is_online = True
print("Value of  is_online " + str(is_online))

# Exercise Calculator
# Number 1
# Number 2
# Sum

first = 10
second = 20
result = first + second
print("result :-", result)

first = 10
name = "John Doe"
sec_result = first + name  # unsupported operand type(s) for +: 'int' and 'str'
print(sec_result)
third_result = name + first  # can only concatenate str (not "int") to str
print(third_result)
