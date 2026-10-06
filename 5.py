# File Handling

# File Modes ##########
# "r" = Read = Opens an existing file for reading
# "r+" = Read + Write
# "w" = Write = Writes data to the file and if the file already contains data, "W" delete the old one
# "a" = Append = Adds new data at the end of the file and existing data stays
# "a+" = Append = add and read both
# "x" = Create a new file = Creates a new file.

#file read ############
# file = open("test.txt","r")
# data = file.read()
# # data = file.readline()
# print(data)
# file.close()

# file write ############
# file = open("test.txt","w")
# data = file.write("hru?") # it changes in our file
# file.close()

#file append
# file = open("test.txt","a")
file = open("test.txt","a+")
file.write("python is easy\n")
file.seek(0)
data = file.read()
print(data)
file.close()
