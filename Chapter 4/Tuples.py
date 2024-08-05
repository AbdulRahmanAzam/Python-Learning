# TUPLES ARE ALSO IMMUTABLE LIKE STRINGS

# a = (1)   # this is integer

a = (1,)  # this is tuple
print(type(a))

b = (1, 2, 3, 4, 5)
len = len(b)

repeat = b * 3

count2 = b.count(2)

concatenate = b + tuple(reversed(b))

index = b.index(5)

reverse = tuple(reversed(b))

print("length: ", len)
print("repeat: ", repeat)
print("count of 2: ", count2)
print("concatenate: ", concatenate)
print("index: ", index)
print("reverse: ", reverse)

for element in b:
    print(element)

