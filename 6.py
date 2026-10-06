# Error handlaing
# it allow us to handle unexpected situation
# Different error names tell Python what kind of problem you are expecting and how you want to handle it.


# try and except ############
# try:
#     num = int(input("Enter a number = "))
#     print(num)
# except :
#     print("Enter a valid num")


# Handling a Specific Error ###########
# try:
#     num = int(input("Enter a number = "))
#     print(num)
# except ValueError:  # Handle invalid value
#     print("Enter a valid num")


# Multiple except Blocks ##############
# ValueError = Wrong value
# TypeError = Wrong data type
# ZeroDivisionError = Dividing by zero
# FileNotFoundError = File doesn't exist
# IndexError = Invalid list index
# KeyError = Dictionary key doesn't exist
# NameError = Variable doesn't exist

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print(result)
# except ValueError:
#     print("Please enter numbers only")
# except ZeroDivisionError:  # Handle division by zero
#     print("num2 cant be 0")


# else #############
# The else block runs only when there is no error.
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print("You entered:", num)


# finally ############
# finally block always executes, whether there is an error or not.
# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("Invalid number")
# finally:
#     print("Program finished")


# Raising Your Own Error with raise ############
# it creates an error manually
# try:
#  age = int(input("Enter your age: "))
#  if age < 18:
#     raise ValueError("Age must be 18 or above")
#  print("You are eligible")
# except ValueError as e:
#   print(e)


#File Handling + Error Handling ###########
try:
    file = open("test.txt", "r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File does not exist")