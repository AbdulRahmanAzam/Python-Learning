f = open("Chapter 9/poems.txt", "r")

# line = f.readline()
# while(line != ""):
#     word = line.split()
#     for st in word:
#         if(st == "twinkle"):
#             print("True twinkle is present")
#     print(word) 
#     line = f.readline()


 # Same work
content = f.read()
if "twinkle" in content:
    print("Twinkle is present")
