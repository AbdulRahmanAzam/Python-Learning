words = ["donkey", "wow", "great"]

with open("Chapter 9/donkey.txt", "r") as f:
    text = f.read()
    
for word in words:
    text = text.replace(word, "#" * len(word))

with open("Chapter 9/donkey.txt", "w") as f:
    f.write(text)

