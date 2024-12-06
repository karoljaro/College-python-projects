from helpers import terminal
from random import randint

def get_randomNum() -> int:
    return randint(33, 126)

def get_userPassLength() -> int:
    while True:
        try:
            passLength: int = int(input("Wprowadź jaką długość ma mieć hasło: "))

            return passLength
        except (ValueError, TypeError):
            print("------------------\nPodana wartość nie jest liczbą")
            continue
        except Exception as err:
            print(f"------------------\nNiespodziewany błąd: {err}")
            continue


def generatePass(passLength: int) -> str:
    passwd: str = ''
    for _ in range(passLength):
        passwd += chr(get_randomNum())
    
    return passwd
        

def main() -> None:
    terminal.clear()
    passLength: int = get_userPassLength()
    print(f"Twoje hasło to:\t {generatePass(passLength)}")


if __name__ == "__main__": main()



