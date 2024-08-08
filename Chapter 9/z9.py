with open("Chapter 9/this.txt") as f1:
    file1 = f1.read()

with open("Chapter 9/copy.txt") as f2:
    file2 = f2.read()

if file1 != file2:
    print("The file doesnt match")
else:
    print("The file matches")