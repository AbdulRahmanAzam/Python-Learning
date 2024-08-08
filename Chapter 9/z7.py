with open("Chapter 9/log.txt") as f:
    lines = f.readlines()

count = 1
for line in lines:
    count += 1
    if "python" in line:
        print("present at : ", count)