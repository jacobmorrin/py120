"""
p:
Create an object-oriented number guessing class for numbers in the range 
1 to 100, with a limit of 7 guesses per game. The game should play like this:

rules & restrictions:
- numbers between 1-100
- 7 guessses

- input
- numbers

- output
Your guess is too low.
Your guess is too high.

e:


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

data:
- random number generated between 1-100
- Boolean to show if number to high too low
- avoid strings
- avoid numbers outside range
- keep track of guesses with instance variable

a:

"""
import random

class GuessingGame:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.answer = random.randint(1, 100)
        self.remaining = 7

    def play(self):
        self.reset()
        while self.remaining > 0:
            print(f"You have {self.remaining} guesses remaining.")
            guess = self.validate()
            self.remaining -= 1
            guess_result = self.high_low_match(guess)


            if guess_result == 'match':
                print(f"\nYou got it! {self.answer} was correct!")
                return
            
            if guess_result == 'high':
                print(f"\nYou're guess is too high. {self.remaining} guesses left")
            else:
                print(f"\nYou're guess is too low. {self.remaining} guesses left!")

        if guess_result == 'match':
            print(f"You got it! {self.answer} was correct!")
        elif guess_result == 'high':
            print(f"You're guess is too high. No guesses left!\n")
        elif guess_result == 'low':
            print(f"You're guess is too low. {self.remaining} guesses left!\n")

    def validate(self):
        while True:
            guess = input("Enter a number between 1 and 100: ")
            try:
                guess = int(guess)
            except ValueError: 
                print("Please only enter integers!")
                continue
            
            if guess < 1 or guess > 100:
                print("Please only input integers between 1 and 100! Try again!")
            else:
                return guess
    
    def high_low_match(self, guess):        
        if guess == self.answer:
            return "match"
        elif guess > self.answer:
            return "high"
        elif guess < self.answer:
            return "low"

game = GuessingGame()
game.play()