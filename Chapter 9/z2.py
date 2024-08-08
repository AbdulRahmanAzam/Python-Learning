import random

def game():
    print("Welcome to the game!")
    score = random.randint(1, 100)

    print(f"Your score is {score}")

    with open("Chapter 9/game.txt") as f:
        high = f.read()
        
        if(high != ""):
            high = int(high)
        else:
            high = 0

    if(high < score):
        high = score

    with open("Chapter 9/game.txt", "w") as f:
        f.write(str(high))
    
    print(f"The highscore is {high}")

    return high
    

game()