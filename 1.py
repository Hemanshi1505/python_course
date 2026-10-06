# variable - Python automatically understands the data type ##########
name = "Hemanshi"  # string
age = 20  # integer
height = 5.5  # float
is_student = True  # boolean

# print #############
# print(name,age,height,is_student);

# Checking the Data Type #######
# print(type(height));

# Taking Input From the User ###########
# value = input("enter your name : "); #input() Always Returns a String
# print("hello dear", value);

# Type Conversion ##########
# print(int(20.20));
# print(float(20));
# print(str(20));
# print(bool(20));

# sum ########
# num1 = int(input("Enter 1 number = "));
# num2 = int(input("Enter 2 number = "));
# num3 = int(input("Enter 3 number = "));
# num = num1 + num2 + num3
# print(num);

# Fahrenheit formula #########
# Celsius = int(input("enter Celsius = "));
# Fahrenheit = (Celsius * 1.8) + 32;
# print("Fahrenheit = ", Fahrenheit);

# if else ##########
# value = int(input("Enter a number : "));
# if value % 2 == 0:
#     print("even num");
# elif value % 2 == 1;
#     print("odd num");
# else :
#     print("something wong");

# and,or,not #########
# value1 = int(input("Enter a number 1: "));
# value2 = int(input("Enter a number 2: "));

# if value1 == 0 and value2 == 0 :
#     print("true");
# else :
#     print("false");

# is_rain = False;
# if not is_rain: #not
#     print("Go outside");

# Login system ##########
# name = str(input("Enter a name = "));
# password = int(input("Enter a password = "));

# if name == "hemanshi" and password == 12345 :
#     print("Login success");
# else :
#     print("Login Fail");

# Nested if ###########
# age = int(input("Enter a age = "));
# if age >= 18 :
#     if age >= 50 :
#         print("you are senior sitizen");
# else :
#         print("you are young");
# else :
#     print("you are minor");

# student result
name = str(input("Enter student name =  "))
maths = int(input("Enter marks for maths = "))
sci = int(input("Enter marks for science = "))
eng = int(input("Enter marks for English = "))

marks = maths + sci + eng
percentage = (marks / 300) * 100
print("percentage = ", percentage)
if percentage >= 50:
    print("Pass")
else:
    print("Fail")
