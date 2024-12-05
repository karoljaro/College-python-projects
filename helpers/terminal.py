import os
import platform

def clear():
    # if platform.system() is "Windows":
    #     os.system('cls')
    # else:
    #     os.system('clear')

    os.system('cls' if platform.system() is "Windows" else 'clear')

   