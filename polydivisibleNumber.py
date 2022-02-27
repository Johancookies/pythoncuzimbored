from helpers import *

def polydivisibleNumber():
    while True:
        clearConsole()
        print(msg(f"Problema 2 - Números polisivisibles : \n"))
        numbersApproved = 0 # Cuenta la cantidad de divisones posibles para el numero
        number = input(msg("Digite un numero => "))
        if number.isdigit():
            startingLen = len(number) 
            number = int(number)
            while True:
                currentOperation = number / (len(str(number))) # Guarda el resultado de la operacion actial
                if currentOperation.is_integer() and currentOperation < 10**18: #Verifica si es entero y no exede 10**18
                    numbersApproved += 1 # Cuenta una divion con resultado entero
                    if len(str(number)) == 1: # Termina el proceso si solo es de una cifra el numero
                        break
                    else: 
                        number = int(str(number)[:-1]) # Eetira la ultima cifra del numero
                else: 
                    break
        else:
            print(fail("Numero invalido"))
        print(ok("\nPOLIDIVISIBLE" if numbersApproved == startingLen else fail("\nNO POLIDIVISIBLE"))) 
        input("\n\nPresiona enter para continuar...")
        break
    
polydivisibleNumber()