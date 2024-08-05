str = "Abdul Rahman Azam"


# Finds length 
len = len(str)
print(len)

# Check whether the string ends with it or not
check = str.endswith("am")
print(check)

# counts total no of occurences
count = str.count("a") # not counts the capital if given small alphabet
print(count)

# capitalize the first letter
capitalize = str.capitalize()
print(capitalize)

# It finds the given word present in the string
find = str.find("man") # returns its first occurence's index
print(find)

# It replaces all the letter with the another
replace = str.replace("a", "0")
print(replace)


# THERE ARE MANY OTHER FUNCTIONS AS WELL