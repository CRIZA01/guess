# GuessTheNumberGame
import random
print("Hello, What your name?")
my_name = input()

number = random.randint(1, 100)
win = False

while not win:
    guess = int(input("Guess the number: "))

    if guess > number:
        print(my_name + " your guess is too high.")
    elif guess < number:
        print(my_name + "your guess is too low.")
    else:
        print("congrats,you have guess the correct number, and won the game")
        win = True
