total = 0
flag = True

for i in range(3):
    marks = int(input("Enter sub marks:  "))
    if(marks < 33):
        flag = False
    total += marks

total /= 3
if(total < 40):
    flag = False

print("Does this student passed? ", flag)
