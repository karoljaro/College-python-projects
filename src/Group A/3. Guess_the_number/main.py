from helpers import terminal
from random import randint

def choice_valid(randomNum: int, guessChoice: int) -> bool:
    if not randomNum or not guessChoice:
        raise ValueError("RandomNum or guessChoice is propably NULL")

    if randomNum > guessChoice:
        print("Szukana liczba jest większa od twojej")
        return False
    elif randomNum < guessChoice:
        print("Szukana liczba jest mniejsza od twojej")
        return False
    else:
        print(f"\n\nGratuluje, znalazłeś szukaną liczbę, która wynosi: {randomNum}")
        return True

def main() -> None:
    terminal.clear()
    randomNum: int = randint(0, 100)
    trials: int = 0

    while True:
        try:
            numChoose: int = int(input("Wpisz liczbę (0 - 100): "))
            assert 0 <= numChoose <= 100
            trials += 1
            if choice_valid(randomNum, numChoose): break

        except ValueError as err:
            print(f"Błąd {err}")
        except AssertionError:
            print("Liczba musi być w zakresie od 0 do 100")
    
    print(f"Liczba twoich prób wynosi: {trials}")

if __name__ == "__main__": main()