import random
'''
1 for snake
-1 for water
0 for gun
'''

# gun kill snake
# snake kill water
# water kill gun

computer = random.choice([-1, 0, 1])

char = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

reversechar = {
    1 : "snake",
    -1 : "water",
    0 : "gun" 
}

you = input("Enter your choice (s, w, g): ")

print(f"You chose: {reversechar[char[you]]} \ncomputer chose: {reversechar[computer]}")

you = char[you]
if(computer == you):
    print("Its a draw")

if(computer == 0 and you == 1):
    print("Computer Wins")

elif(computer == 1 and you == -1):
    print("Computer Wins")

elif(computer == -1 and you == 0):
    print("Computer Wins")

else:
    print("Congrats! You won")