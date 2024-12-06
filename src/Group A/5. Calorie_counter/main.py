from helpers import terminal
from typing import TypedDict, Optional

class UserData(TypedDict):
    foodName: str
    callorie: int

def get_userData() -> Optional[list[UserData]]:
    userdata: list[UserData] = []
    try:
        while True:
            foodName: str = input("\nWpisz nazwę jedzenia: ")
            callorie: int = int(input("Wpisz ile kalori posiada te jedzenie: "))
        
            userdata.append({
                "foodName": foodName,
                "callorie": callorie
            })

            cancelAdd = input("Jeżeli chcesz zakończyć dodawanie rzeczy naciśnij 'n', a potem zatwierdz enterem ")
            if cancelAdd == 'n': break
        
        return userdata
    except (ValueError, TypeError):
        print(f"Dane powinny być w odpowiednim typie ")
    except Exception as err:
        print(f"Niespodziewany błąd: {err}")

    return None

def sumCalorie(data: list[UserData]) -> int:
    sum: int = 0
    for position in data:
        sum += position['callorie']
    
    return sum

def showResult(data: list[UserData]) -> None:
    terminal.clear()
    for singeData in data:
        print(f"- {singeData['foodName']}: {singeData['callorie']} kolorii")

    print(f"-----------------------------")
    print(f"Zjadłeś dzisiaj {sumCalorie(data)} kolorii")

def main() -> None:
    terminal.clear()
    data = get_userData()

    showResult(data) if data else print("Brak danych")

if __name__ == "__main__":
    main()
