
import random

def requestNumber():
    while True:
        number = input('Introduce un numero del 1 al 10: ')
        if number.isdigit():
            return int(number)
        else:
            print('Por favor introduce un numero valido')

def game():
    intentos = 0
    key = random.randint(1,10)
    adivinado = False

    while not adivinado:
        number = requestNumber()
        intentos+=1
        if number > key:
            print('El numero secreto es menor')
        elif number < key:
            print('El numero secreto es mayor')
        else:
            print(f'Felicidades, el numero es {key}')
            print(f'Intentos = {intentos}')
            adivinado = True

game()

    