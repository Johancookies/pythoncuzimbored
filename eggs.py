from helpers import *

def digits():
    while True:
        clearConsole()
        print(msg(f"Problema 4 - Cociendo huevos \n"))
        while True: # Valida la cantidad de huevos
            eggs = input(msg("Digite la cantidad de huevos => "))
            if eggs.isdigit():
                eggs = int(eggs)
                break
            else: 
                print(fail("Numero invalido"))
        while True: # Valida la capacidad en huevos
            capacity = input(msg("Digite la capacidad de la olla (en huevos) => "))
            if capacity.isdigit():
                capacity = int(capacity)
                break
            else: 
                print(fail("Numero invalido"))
        minutes = 1
        eggCount = 0
        for x in range(eggs - 1):
            eggCount += 1
            if eggCount == capacity: # Aumenta la cantidad de minutos cuando los huevos igualan la capacidad
                minutes += 1
                eggCount = 0
        if capacity == 0 and eggs == 0:
            break
        else:
            print(ok(f"El tiempo de coccion es de {minutes * 10} minutos"))
            endRun()
    endRun()

digits()