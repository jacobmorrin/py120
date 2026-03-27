"""
problem:
Create an object-oriented number guessing class for numbers in the range 1 to 100, 
with a limit of 7 guesses per game. The game should play like this:

input:

boundaries:
Note that a game object should start a new game with a new number to guess with each call to play.


algo-hl
set constants for:
    # guesses
    # high message
    # low message
    # win message

initialize the object by resetting everything
reset the number of guesses
initiate the game (play)
    - ask for user input
validate user input
test whether user input is high, low, or a match


game = GuessingGame()
game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 104
Invalid guess. Enter a number between 1 and 100: 50
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 1 and 100: 75
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 85
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 0
Invalid guess. Enter a number between 1 and 100: 80
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 81
That's the number!

You won!

game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 50
Your guess is too high.

You have 6 guesses remaining.
Enter a number between 1 and 100: 25
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 37
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 31
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 34
Your guess is too high.

You have 2 guesses remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have 1 guess remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have no more guesses. You lost!

problem

set constants for:
    # guesses
    # high message
    # low message
    # win message

initialize the object by resetting everything
reset the number of guesses
initiate the game (play)
    - ask for user input
validate user input
test whether user input is high, low, or a match

"""
import random 

class GuessingGame():
    MAX_GUESSES = 7
    GUESSES_REMAINING = range(MAX_GUESSES, 0, -1)

    GUESS_RANGE_START = 1
    GUESS_RANGE_END = 100

    MESSAGES = {
        'HIGH': 'Your guess is too high.',
        'LOW': 'Your guess is too low.',
        'MATCH': "That's the number! You've won!",
    }

    ENTER_GUESS = f"Enter a number between {GUESS_RANGE_START} and {GUESS_RANGE_END}: "

    def show_guesses_remaining(self, guesses):
        plural = "guesses" if guesses > 1 else "guess"
        print(f"You have {guesses} {plural} left.\n")
    
    def __init__(self):
        self.secret_number = None

    def reset(self):
        self.secret_number = random.randint(self.GUESS_RANGE_START, self.GUESS_RANGE_END)

    def validate_guess(self):
        while True:
            guess = input(self.ENTER_GUESS)
            if not guess.isdigit():
                 print("Only digits please!\n")
                 continue
            
            guess = int(guess)

            if guess not in range(self.GUESS_RANGE_START, self.GUESS_RANGE_END + 1):
                 print(f"Please enter a digit between {self.GUESS_RANGE_START} and {self.GUESS_RANGE_END}.\n")
                 continue
            return guess
    
    def check_guess(self, guess):
        if guess > self.secret_number:
            return 'HIGH'
        elif guess < self.secret_number:
            return 'LOW'
        else:
            return 'MATCH'

    def play(self):
        self.reset()

        for remaining_guesses in self.__class__.GUESSES_REMAINING:
            self.show_guesses_remaining(remaining_guesses)
            guess = self.validate_guess()
            result = self.check_guess(guess)
            print(self.MESSAGES[result])
            
            if guess == self.secret_number:
                return
            
        print(f"You're out of guesses! The secret number was: {self.secret_number}.")
        
game = GuessingGame()
game.play()