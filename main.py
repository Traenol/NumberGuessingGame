import random

def main():
    print("Welcome to the number guessing game.")
    number_to_guess = random.randint(1,100)
    print("I have thought of a number between one and one hundred.")
    print("What number do you think it is?")
    current_guess = 0
    guess_counter = 0
    while current_guess != number_to_guess:
        current_guess = ""
        while not current_guess.isdigit():
            print("Please enter a number. No letters, only digits.")
            current_guess = input()
        guess_counter += 1
        current_guess = int(current_guess)
        if current_guess == number_to_guess:
            print(f"Correct! it took you {guess_counter} tries")
        elif current_guess > number_to_guess:
            print("Too high")
        elif current_guess < number_to_guess:
            print("Too low")
        else:
            print("Wrong, try again.")

main()