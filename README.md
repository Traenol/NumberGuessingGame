# Week 2: Project 1 - Number Guessing Game
A simple CLI guessing game to practice core Python control flow, loops, and input handling.
The player chooses a difficulty, a number will be picked, and player will be given feedback after every guess. Upon guessing the correct number, the player will win and will be asked if they wish to continue playing.

## Project Requirements

- Use random module
- Primary game loop to guess the correct number
- Provide High and low feedback
- Win message on successful guess

## Secondary features

- Difficulty levels
- Guess counter
- Replay option

## Usage Instructions

- Must have Python3 installed
- Clone this repository
- run: python main.py

## What I learned

- Handling user input safely
- Preventing infinite loops
- Using dictionaries to manage data
- Code separation into functions

## Example Gameplay

```
Welcome to the number guessing game.
Please select a difficulty:
1: Easy(1-10)
2: Moderate(1-50)
3: Challenging(1-100)
4: Difficult(1-255)
5: Extreme(1-1000)
6: Insane(1-50000)
7: Good Luck(1-1000000)
8: Random
1
I have thought of a number between 1 and 10.
What number do you think it is?
Please enter a number. No letters, only digits.
5
Too high
Please enter a number. No letters, only digits.
3
Correct! it took you 2 tries
Would you like to play again? Y/N
n
```

## Future Improvements
- Add unit tests
- Implement scoring system
- Add limited attempts for difficulty