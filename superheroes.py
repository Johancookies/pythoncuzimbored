from helpers import *

def superheroes():
    clearConsole() 
    print(msg("Problema 7 - Transformación de superhéroes\n"))
    data = getCharacters()
    heroes = ["*", "+"]
    validCount = 0
    while True:
        name = input(msg(f"Digite el nombre del superheroe {validCount + 1} => "))
        if verifyName(name, data) and heroes[0] != name:
            heroes[validCount] = name
            validCount += 1
        else:
            print(fail("El nombre no es valido"))
        if validCount >= 2 and len(heroes[0]) == len(heroes[1]):
            break
    print(ok("Si") if verifyChange(heroes) else fail("No"))
    endRun()

# Verifica el numero de vocales y consonantes en cada heroe
def verifyChange(heroes):
    vocals = ["a", "e", "i", "o", "u"]
    counts = []
    for hero in heroes:
        vocalsCount = 0
        consonantsCount = 0
        for x in hero:
            if x in vocals:
                vocalsCount += 1
            else:
                consonantsCount += 1
        counts.append(vocalsCount)
        counts.append(consonantsCount)
    return True if counts[0] == counts[2] and counts[1] == counts[3] else False
    
# Verifica que el nombre cumpla las condiciones
def verifyName(name, data):
    valid = 0
    for currentCharacter in name:
        if currentCharacter in data:
            valid += 1
    return True if valid == len(name) else False

# obtinene valores permitidos para el nombre de los superheroes
def getCharacters():
    characterCode = 97
    data = []
    while characterCode < 123:
        data.append(chr(characterCode))
        characterCode += 1
    data.append("ñ")
    return data
 
superheroes()