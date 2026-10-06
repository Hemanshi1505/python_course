# Functions, String

#def means define a function.
def welcome():
    print("hello")
    print("Welcome to python")

# sum without parameter ###########
def sum():
    val1 = int(input("Enter a value1 = "))
    val2 = int(input("Enter a value2 = "))
    add = val1 + val2
    print(add)


# multiply with parameter
# def multiply (val1,val2):
#     mul = val1*val2
#     print(mul)
# val1 = int(input("Enter a value1 = "))
# val2 = int(input("Enter a value2 = "))

# multiply(val1,val2)

# return ############
def check(year):
    if year % 4 == 0: 
        return "it's a leap year"
    else:
        return "it's not a leap year"

year = int(input("Enter a year = "));
result = check(year)
print(result)

# string #############
# upper()	Convert to uppercase
# lower()	Convert to lowercase
# capitalize()	Capitalize first character
# title()	Capitalize every word
# strip()	Remove spaces from both sides
# replace()	Replace text
# find()	Find position
# count()	Count occurrences
# split()	String → List
# join()	List → String
# startswith()	Check beginning
# endswith()	Check ending