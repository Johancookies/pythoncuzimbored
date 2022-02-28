import os
import platform
command = "cls" if platform.system() == "Windows" else "clear"
clear = lambda: os.system(command)

def clearConsole(): #Limpia la consola
    return clear()

# Colores de texto
def fail(text):
    return '\033[91m' + text + '\033[0m'

def ok(text):
    return '\033[92m' + text + '\033[0m'

def msg(text):
    return '\033[95m' + text + '\033[0m'

# Mensaje final
def endRun():
    input(msg("\nPresione una tecla para continuar..."))


