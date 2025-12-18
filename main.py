import random
DIFFICULTY = {1: ["1: Easy(1-10)",1,10],
              2: ["2: Moderate(1-50)",1,50],
              3: ["3: Challenging(1-100)",1,100],
              4: ["4: Difficult(1-255)",1,255],
              5: ["5: Extreme(1-1000)",1,1000],
              6: ["6: Insane(1-50000)",1,50000],
              7: ["7: Good Luck(1-1000000)",1,1000000],
              8: ["8: Random",1,7],}

def main():
    print("Welcome to the number guessing game.")
    playing = True
    while playing:
        diff = get_difficulty()
        if diff == 8:
            diff = get_number_to_guess(DIFFICULTY[diff][1], DIFFICULTY[diff][2])
        min = DIFFICULTY[diff][1]
        max = DIFFICULTY[diff][2]
        start_game(get_number_to_guess(min, max), min, max)
        print("Would you like to play again? Y/N")
        play_again = ""
        while play_again != "n" or play_again != "y":
            play_again = input()
            if play_again.lower() == "n":
                playing = False
                break
            elif play_again.lower() == "y":
                break
            else:
                print("Please enter either Y/N only/")
    
def get_difficulty():
    print("Please select a difficulty:")
    for diff in DIFFICULTY:
        print(f"{DIFFICULTY[diff][0]}")
    difficulty = 0
    while difficulty < 1:
        difficulty = input()
        if not difficulty.isdigit():
            difficulty = 0
            print("Please enter a number between 1 and 8")
        else:
            difficulty = int(difficulty)
    return difficulty

def get_number_to_guess(min, max):
    return random.randint(min, max)

def start_game(number_to_guess, min, max):
    print(f"I have thought of a number between {min} and {max}.")
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