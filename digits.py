from helpers import *

def digits():
    while True:
        clearConsole()
        print(msg(f"Problema 5 - Suma de dígitos \n"))
        number = input(msg("Digite un numero => "))
        if number.isdigit():
            result = 0
            operation = ""
            for currentNumber in number:
                result += int(currentNumber)
                operation += f" {currentNumber} +"
            break
        else:
            print(fail("Numero invalido"))
    operation = operation[:-1] 
    print(ok(f"{operation}= {result}"))
    endRun()
    
digits()