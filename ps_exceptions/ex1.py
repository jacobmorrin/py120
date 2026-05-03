def convert_to_float(num):
    try:
        num = float(num)
        return num
    except ValueError as e:
        print(f'ValueError:{e}. Only numbers please. {num} is not a number.')

num1 = input('Enter first number: ')
num1 = convert_to_float(num1)
num2 = input('Enter second number: ')
num2 = convert_to_float(num2)

try:
    print(f'{num1 / num2}')
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}. Looks like you tried to divide by zero! Unfortunately that's impossible!")

