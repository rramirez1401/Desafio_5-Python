import platform
import os

def limpiar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")