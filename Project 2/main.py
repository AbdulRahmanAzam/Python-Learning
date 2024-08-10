from random import randint

count = 1
guess = int(input("Enter your guess: "))
num = randint(1, 100)

while(guess != num):
    if(guess > num):
        print("Lower number please")
    else:
        print("Higher number please")
    
    count += 1
    guess = int(input("\nEnter your guess: "))

print(f"You successfully found the {num} in {count} attempts")
