list = ["Make a lot of money", "buy now","subscribe this", "click this"]
s = "buy now"
flag = False
for elements in list:
    if(elements == s):
        flag = True
        break

print("Is it a scam? : ", flag)