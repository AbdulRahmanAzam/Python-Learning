with open("Chapter 9/log.txt") as f:
    text = f.read()

if "python" in text:
    print("found python")