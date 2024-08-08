st = "Hello my name is Abdul Rahman Azam"

# f = open("file.txt", "w")
# f.write(st)
# f.close()



# f = open("file.txt", "r")
# print(f.read())
# print(f.readlines())
# f.close()



# f = open("file.txt", "r")
# line = f.readlines()

# while(line != ""):
#     print(line)
#     line = f.readline()





# f = open("file.txt", "r")
# print(f.read())
# f.close()

# The same can be done by using WITH statement
with open("Chapter 9/file.txt") as f:
    print(f.read())

# No need for f.CLOSE()