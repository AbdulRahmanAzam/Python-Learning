arr = ["asad", "azam","basit","rahman","pasha","tariq"]
find = "tariq"
flag = False

for elements in arr:
    if(elements == find):
        flag = True

print(f"is {find} found?", flag)
