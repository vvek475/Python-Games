import random
"""
def guess(x):
    random_numbers=random.randint(1,x)
    guess=0
    while(guess!=random_numbers):
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess <random_numbers:
            print("sorry guess is too low")
        elif guess>random_numbers:
            print("sorry too high")
    print(f"Conrats it's {random_numbers}")
guess(10)"""
def computer_guess(x):
    low,high,feedback=1,x,""
    while feedback != "c" and low!=high:
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high (H) ,too low (L),or correct (c)??')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'yay crrct {guess}')
computer_guess(10)