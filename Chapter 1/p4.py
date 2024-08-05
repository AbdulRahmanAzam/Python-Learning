import os

# select the path of which you want to display its contents
directory_path = '.'

# using os module to list the directory from path given
contents = os.listdir(directory_path)

# printing the contents
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)
