import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Hey, this number is too low, try again a higher one! ")
        elif guess > random_number:
            print("Well, you went too high, try a lower one :) ")

    print("Way to go! you have guessed it!!!")

guess(10)