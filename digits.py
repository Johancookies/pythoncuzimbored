from helpers import *

def digits():
    while True:
        clearConsole()
        print(msg(f"Problema 5 - Suma de dígitos \n"))
        number = input(msg("Digite un numero => "))
        if number.isdigit():
            result = 0 # Guarda el total de la suma
            operation = "" # Guarda la suma de todos
            for currentNumber in number:
                result += int(currentNumber)
                operation += f" {currentNumber} +"
            break
        else:
            print(fail("Numero invalido"))
    operation = operation[:-1] # elimina el "+" sobrante
    print(ok(f"{operation}= {result}"))
    endRun()
    
digits()