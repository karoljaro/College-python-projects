from helpers import terminal

def calculate_bmi(weigth: float, heigth: float) -> float:
    if weigth <= 0 or heigth <= 0:
        raise ValueError("Waga i wzrost muszą być większe od zera")

    return weigth / (heigth ** 2)

def interpret_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        return "Waga prawidłowa"
    elif 25 <= bmi < 29.9:
        return "Nadwaga"
    else: 
        return "Otyłość"


def main() -> None:
    try:
        terminal.clear()
        heigth: float = float(input("Wprowadź jaki masz wzrost: "))
        weigth: float = float(input("Wprowadź jaką masz wagę: "))

        bmi = calculate_bmi(weigth, heigth)
        interpretation = interpret_bmi(bmi)

        print(f"Twoje BMI wynosi {bmi:.2f}", end="\n")
        print(f"Interpretacja: {interpretation}", end='\n')

    except ValueError as err:
        print(f"Błąd: {err}")


if __name__ == "__main__": main()