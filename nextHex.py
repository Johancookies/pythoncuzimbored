from helpers import *

values = [
    "1", "2", "3", "4", "5", "6", "7", "8",
    "9", "A", "B", "C", "D", "E", "F", "0", "1"
]

def nextHex():
    clearConsole()
    print(msg("Problema 1 - Súmale uno"))
    for counter in range(3): 
        while True:
            number = input(msg(f"\nDigite un numero en hexadecimal (caso {counter + 1}/3) => "))
            isValid = validateInput(number)
            if (len(number) < 3 and isValid):
                if len(number) == 1:
                    result = changeCharacter(number[0])
                elif len(number) == 2:
                    result = number[0]
                    currentResult = changeCharacter(number[1])
                    if currentResult == "0":
                        result = changeCharacter(number[0])
                    result += currentResult
                if result == "00":
                    result = "100"
                print(ok(f"{number} => {result}"))
                break
            else:
                print(fail("El numero no es valido"))

    endRun("FIN\n\nPresione una tecla para continuar...")
            
def changeCharacter(character):
    if character in values:
        character = values[values.index(character) + 1]
    return character

def validateInput(number):
    isValid = True
    for character in number:
        if not character in values:
            isValid = False
    return isValid

nextHex()