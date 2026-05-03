"""
Write a program that asks the user for a number. If the input isn't a number, 
let Python raise an appropriate exception. If the number is negative, raise a 
ValueError with an appropriate error message. If the number isn't negative, 
print a message that shows its value.
"""

num = float(input("Enter a number: "))

if num < 0:
    raise ValueError('Negative number.')
print(f'The value is {num}')

