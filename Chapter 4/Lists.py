# LISTS ARE MUTABLE, unlike strings

l1 = [5, "hundred", True, 33.333, None]
print(l1)

l1[2] = "changed"
print(l1)


print("Now printing l2\n\n")

l2 = [5, 200, 45, 99, 34]
print("before sort:  ", l2)

l2.sort()
print("After sort:  ", l2)

l2.pop()
print("pop:  ", l2)

l2.reverse()
print("Reverse:  ", l2)

l2.append(33)
print("Appending 33", l2)

