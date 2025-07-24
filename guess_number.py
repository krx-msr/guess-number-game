import random

print("Welcome to Guess the Number!")
number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {number}. You guessed it in {attempts} tries.")
        break
