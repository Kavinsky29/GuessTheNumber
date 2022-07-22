import random

#The computer will guess the number you have in mind up to 100000000 !! :)
 
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Excellent! The machine guessed the number you had in mind: {guess} !!!!')

computer_guess(100000000)