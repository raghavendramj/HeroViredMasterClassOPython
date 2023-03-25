# Exercise 2
#
# A employee joined the company named John Adams
# His age is 20 years old
# He is a new employee
# create variables for all of them, and make a statement and print it.

emp_name = "John Adams"
age = 20
emp_type = "New Employee"
print("A person named " + emp_name + " has joined the organisation aged " + str(age) + " and he/she is a " + str(
    emp_type))

# Receiving input from user
name = input("What is your name? ")
print("Welcome " + name)

# Exercise 3
# Take user input for birth year and print his/her actual age.
birth_year = input("Please Enter your birth year? ")

# type conversion
age = 2023 - int(birth_year)
print("Your current age is " + str(age))


