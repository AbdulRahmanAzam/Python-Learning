def greater(a, b=0, c=0):
    ans = 0
    if(a >= b and a >= c):
        ans = a
    elif(b >= a and b >= c):
        ans = b
    else:
        ans = c

    return ans


res = greater(5,7,9)
print(res)