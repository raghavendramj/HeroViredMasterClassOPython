# Exercise 4
# Take input from user first and second
# print the product

print("*********** SIMPLE CALCULATOR *************")
first = input("First Number :- ")
second = input("Second Number :- ")
result = int(first) * int(second)  # if input is float -> 10.23 -> invalid literal for int() with base 10: '12.123'
print("1. Result :- " + str(result))

# int -> float -> Valid
# float -> int -> Invalid

third = float(input("Third Number :- "))
fourth = float(input("Fourth Number :- "))
result = third * fourth
print("2. Result :- " + str(result))
