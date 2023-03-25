# strings


# Immutable Strings
str = "Raghav"  # Memory: -"Raghav"
str = "Raghavendra"  # Memory: -"Raghav", "Raghavendra"
str = "Raghava"  # Memory: -"Raghav", "Raghavendra", "Raghava"
str2 = "Raghav"  # Memory: -"Raghav", "Raghavendra", "Raghava"

course = "Python For Beginners";

# upper
print("NOTE:- These functions doesn't modify original strings");
print("0. course :- ", course)
print("a. course.upper() :- ", course.upper())
print(" *** 1. course :- ", course)

# lower
print("b. course.lower() :- ", course.lower())
print(" *** 2. course :- ", course)

# find
print("c. course.find('y') :- ", course.find('y'))
print("d. course.find('Y') :- ", course.find('Y'))  # case sensitive

# replace
print("e. course.replace('n', '4') :- ", course.replace('n', '4'))
print(" *** 3. course :- ", course)

# in -> contains
# course = "Python For Beginners";
containsPython = "Python" in course
print("containsPython -> ", containsPython)
containsPython = "PyThon" in course
print("containsPython -> ", containsPython)  # case sensitive
