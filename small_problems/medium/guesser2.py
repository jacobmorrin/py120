"""
In the previous exercise, you wrote a number guessing game that determines a 
secret number between 1 and 100, and gives the user 7 opportunities to guess the number.

Update your solution to accept a low and high value when you create a GuessingGame 
object, and use those values to compute a secret number for the game. You should also 
change the number of guesses allowed so the user can always win if she uses a good strategy. 
You can compute the number of guesses with:
"""
import random
import math

class GuessingGame:

    MESSAGES = {
        'HIGH': 'Your guess is too high.',
        'LOW': 'Your guess is too low.',
        'MATCH': "That's the number! You've won!",
    }

    def show_guesses_remaining(self, guesses):
        plural = "guesses" if guesses > 1 else "guess"
        print(f"You have {guesses} {plural} left.\n")
    
    def __init__(self, low, high):
        self.secret_number = None
        self._low = low
        self._high = high
        self.enter_guess = f"Enter a number between {self._low} and {self._high}: "

    def reset(self, low, high):
        self.secret_number = random.randint(self._low, self._high)
        self.number_of_guesses = int(math.log2(high - low + 1)) + 1
        self.guesses_remaining = range(self.number_of_guesses, 0, -1)

    def validate_guess(self):
        while True:
            guess = input(self.enter_guess)
            if not guess.isdigit():
                 print("Only digits please!\n")
                 continue
            
            guess = int(guess)

            if guess not in range(self._low, self._high + 1):
                 print(f"Please enter a digit between {self._low} and {self._high}.\n")
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
        self.reset(self._low, self._high)

        for remaining_guesses in self.guesses_remaining:
            self.show_guesses_remaining(remaining_guesses)
            guess = self.validate_guess()
            result = self.check_guess(guess)
            print(self.MESSAGES[result])
            
            if guess == self.secret_number:
                return
            
        print(f"You're out of guesses! The secret number was: {self.secret_number}.")
        
game = GuessingGame(501, 1500)
game.play()