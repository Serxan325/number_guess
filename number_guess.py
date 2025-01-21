import random

def number_guess():
    first = int(input("Enter the beginning number: "))
    last = int(input("Enter the finishing number: "))
    trys = int(input("How many times you want to try ?: "))
    number = random.randint(first, last)
    for i in range(trys):
        guess = int(input("What is your guess ?: "))
        if guess == number:
            print("That is correct, you won!")
            break
        else: 
            print("Your answer is not correct.")
            if i == trys - 1:
                print("Game over.")

try:
    number_guess()
except:
    print("An error occured.")
