
import random

def getSecretWord():
    words = ['python','java','javascript','angular','django','react','typescript','git','flask']
    return random.choice(words)

def showProgress(secretWord, guessedLetters):
    guessed = ''
    for letter in secretWord:
        if letter in guessedLetters:
            guessed += letter
        else:
            guessed += '_'
    return guessed

def game():
    secretWord = getSecretWord()
    guessedLetters = []
    attempts = 7
    gameEnd = False

    print('Welcome to the Hangman Game!')
    print(f'You have {attempts} attempts to guess the secret word')
    print(showProgress(secretWord, guessedLetters), 'The amount of letters of the word is:', len(secretWord))

    while not gameEnd and attempts > 0:
        guess = input('Enter a letter: ').lower()

        if len(guess) !=1 or not guess.isalpha():
            print('Please enter a valid letter (Just type a single letter)')
        elif guess in guessedLetters:
            print('You have already used that letter, try again')
        else:
            guessedLetters.append(guess)

            if guess in secretWord:
                print(f'Very well, the letter "{guess}" is present in the word')
            else:
                attempts -= 1
                print(f'Sorry, the letter "{guess}" is not in the word')
                print(f'You have {attempts} attempts left')
            
        currentProgress = showProgress(secretWord, guessedLetters)
        print(currentProgress)

        if '_' not in currentProgress:
            gameEnd = True
            secretWord = secretWord.capitalize()
            print(f'Congratulations, you won! The complete word was: "{secretWord}"')
    
    if attempts == 0:
        print(f'Sorry, You have no attempts left, the secret word was "{secretWord}"')

game()