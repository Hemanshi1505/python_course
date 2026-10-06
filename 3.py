# List[], Tuple(), Set{}, Dictionaries

# [Apple, Banana, Chilly]
#    0      1       2
#   -3     -2      -1

fruits = ["Apple", "Banana", "Orange"]  # List store multiple val in diff types
# stuff = ["Ram", 5, 20.20, True]  # List can store multiple data types
# print(stuff)

# print(stuff[0]); # Accessing List elements
# print(stuff[-1]); # Negative Index

# Adding Element
fruits.append("Mango")
# print(fruits)

# Adding Element on specific position
fruits.insert(1, "Litchi")
# print(fruits)

# Remove element
fruits.remove("Banana")
# print(fruits)

# Remove element on specific position
fruits.pop(0)
# print(fruits)

# Find a length of list
# print(len(fruits));

# Loop thrugh a list
# for i in fruits:
#     print(i)

# check if element exists
# if "Banana" in fruits :
#     print("yess");
# else :
#     print('noo');

# reverse list
fruits.reverse()
# print(fruits);

# sort array
# num = [5,8,3,6,2,1];
# num.sort();
# print(num);

# clear list
# num.clear();
# print(num);

# Task - Student Marks Program ################
# name = str(input("student name = "))
# maths = int(input("Enter a maths mark = "))
# eng = int(input("Enter a english mark = "))
# sci = int(input("Enter a sci mark = "))
# gk = int(input("Enter a gk mark = "))
# hindi = int(input("Enter a hindi mark = "))

# total = [maths, eng, sci, gk, hindi];
# print(total);
# sum = 0;
# for i in total:
#     sum += i;
# print(sum)
# per = (sum / 500) * 100;
# print(per);

# Tuple #############
# Tuple is similar to List but you cant change their value
# len() → returns the number of items.
# count() → counts how many times a value appears.
# index() → finds the position of a value.
data = ("Apple", "Banana", "Litchi", "Mango")
# for i in data:
#     print(i);

# Set ###############
# set stores a unique value
# add()
# remove() → gives an error if the item doesn't exist.
# discard() → does not give an error if the item doesn't exist.
# union() → combines two sets.
# intersection() → returns only common values.
set1 = {10, 20, 30, 20, 40, 50, 10} #Duplicates are automatically removed
# print(set1)

# add an ele
set1.add(60)
# print(set1)

#remove an ele
set1.remove(10)
# print(set1)

# loop through a set
# for i in set1:
#     print(i)

# Dictionaries #############
# A dictionary stores information as {key : value}
student = {
    "name" : "Hemanshi",
    "age" : 20,
    "sex" : "Female"
}
# print(student);
# print(student["name"]);
student['city'] = "Surat"
student["age"] = 21
# print(student)
student.pop("sex")
# print(student)

# loop through dictionaries
# for i in student:
#     print(i)

# loop through key and loop
# for i,v in student.items():
    # print(i, "=", v) 