from random import randint

def play_game():

    print("Hello! What is your name?")

    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")

    num = randint(1, 20)
    guess = int(input())
    k = 1

    while num != guess:
        if guess < num:
            print("Your guess is too low.\nTake a guess.")
            guess = int(input())
            k += 1
        elif guess > num:
            print("Your guess is too high.\nTake a guess.")
            guess = int(input())
            k += 1
    else:
        print(f"Good job, {name}! You guessed my number in {k} guesses!")
