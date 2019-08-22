import random
secret = random.randrange(1, 101)
guess = 0
tries = 0
while guess != secret:
    guess = int(input("make a guess: "))
    tries = tries + 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else: 
        print("You got it!")
print("Number of tries:", tries)