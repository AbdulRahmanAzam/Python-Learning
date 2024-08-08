num = 7
flag = False

for i in range(2, num):
    if(num % i == 0):
        flag = True
        break

print("Is number prime? : ", flag)

