import random

def main():
    print("Welcome to the number guessing game.")
    number_to_guess = random.randint(1,100)
    print("I have thought of a number between one and one hundred.")
    guess = 0
    while guess != number_to_guess:
        print("What number do you think it is?")
        guess = ""
        while not guess.isdigit():
            print("Please enter a number. No letters, only digits.")
            guess = input()
        guess = int(guess)
        if guess == number_to_guess:
            print("Correct!")
        elif guess > number_to_guess:
            print("Too high")
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Wrong, try again.")

main()