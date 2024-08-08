with open("Chapter 9/old11.txt", "r") as f:
    file1 = f.read()

with open("Chapter 9/new11.txt", "w") as f2:
    f2.write(file1)

