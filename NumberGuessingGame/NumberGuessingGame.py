
import random

def requestNumber():
    while True:
        number = input('Enter a number between 1-99: ')
        if number.isdigit():
            if int(number) > 0 and int(number) < 100: 
                return int(number)
            else:
                print('Please enter a number between 1-99')
        else:
            print('Please enter a valid number')

def game():
    attempts  = 0
    key = random.randint(1,100)
    guessed = False

    while not guessed:
        number = requestNumber()
        attempts +=1
        if number > key:
            print('The secret number is lower')
        elif number < key:
            print('The secret number is higher')
        else:
            print(f'Congratulations! The secret number was {key}')
            print(f'Total attempts: {attempts}')
            guessed = True
game()

    