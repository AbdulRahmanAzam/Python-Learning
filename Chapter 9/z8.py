with open("Chapter 9/this.txt") as f:
    copy = f.read()
    with open("Chapter 9/copy.txt", "w") as copyf:
        copyf.write(copy)    