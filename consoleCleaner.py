import os
import platform
command = "cls" if platform.system() == "Windows" else "clear"
clear = lambda: os.system(command)

def clearConsole(): #Limpia la consola
    return clear()