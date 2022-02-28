from helpers import *

def uglyNumber():
    clearConsole() 
    print(msg("Problema 6 - El número feo\n"))
    numbersCount = 0
    currentNumber = 2
    # Cuenta la cantidad de numeros feos hasta que sea 1500, validando sus divisores
    while numbersCount < 1500:
        if (currentNumber % 2 == 0) or (currentNumber % 3 == 0) or (currentNumber % 5 == 0):
            numbersCount += 1
        currentNumber += 1
    print(msg(f"El numero feo 1500 es {currentNumber}"))
    endRun()
        
uglyNumber()