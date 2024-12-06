from helpers import terminal
from typing import TypedDict, Optional

class UserData(TypedDict):
    foodName: str
    callorie: int

def get_userData() -> Optional[UserData]:
    try:
        foodName: str = input("Wpisz nazwę jedzenia: ")
        callorie: int = int(input("Wpisz ile kalori posiada te jedzenie: "))
        
        userData: UserData = {
            "foodName": foodName,
            "callorie": callorie
        }

        return userData 
    except ValueError:
        print(f"Dane powinny być w odpowiednim typie ")
        return None
    except Exception as err:
        print(f"Niespodziewany błąd: {err}")
        return None

def main() -> None:
    terminal.clear()
    data = get_userData()
    if data:
        print("Dane użytkownika:", data)
    else:
        print("Nie udało się uzyskać danych użytkownika.")

if __name__ == "__main__":
    main()