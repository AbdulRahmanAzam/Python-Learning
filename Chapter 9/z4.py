with open("Chapter 9/donkey.txt", "r") as f:
    text = f.read()
    
text = text.replace("donkey", "#####")

with open("Chapter 9/donkey.txt", "w") as f:
    f.write(text)
    
