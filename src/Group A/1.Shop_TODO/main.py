from typing import List, Literal
from helpers import terminal

class Product:
    def __init__(self, name: str, quantity: int) -> None:
        self.name: str = name
        self.quantity: int = quantity
        self.purchased: bool = False

    def __str__(self) -> str:
        status: Literal['kupione'] | Literal['niekupione'] = "kupione" if self.purchased else "niekupione"
        return f"   ● {self.name} - {self.quantity} szt. - {status}"

class ShoppingList:
    # ------------------------| CONSTRUCTOR |------------------------
    def __init__(self) -> None:
        self.products: List[Product] = []

    # ------------------------| ADD |------------------------
    def add_product(self, name: str, quantity: int) -> None:
        self.products.append(Product(name.strip(), quantity))
        print(f"\nStatus:\t Produkt {name} dodany do listy.")
        terminal.printSeperateLine()

    # ------------------------| REMOVE |------------------------
    def remove_product(self, name: str) -> None:
        self.products = [product for product in self.products if (product.name).lower() != name.lower()]
        print(f"\nStatus:\t Produkt {name} usunięty z listy.")
        terminal.printSeperateLine()

    # ------------------------| EDIT |------------------------
    def edit_product(self, name: str, new_name: str, new_quantity: int) -> None:
        for product in self.products:
            if (product.name).lower() == name.lower():
                product.name = new_name if len(new_name) > 0 else name
                product.quantity = new_quantity
                print(f"\nStatus:\t Produkt {name} zaktualizowany na {new_name} - {new_quantity} szt.")
                terminal.printSeperateLine()
                return
        print(f"\nStatus:\t Produkt {name} nie znaleziony na liście.")
        terminal.printSeperateLine()

    # ------------------------| MARK |------------------------
    def mark_as_purchased(self, name: str) -> None:
        for product in self.products:
            if (product.name).lower() == name.lower():
                product.purchased =  not product.purchased
                print(f"\nStatus: \tProdukt {name} oznaczony jako", "kupione" if product.purchased else "niekupione")
                terminal.printSeperateLine()
                return
        print(f"\nStatus: \tProdukt {name} nie znaleziony na liście.")
        terminal.printSeperateLine()

    # ------------------------| SHOW |------------------------
    def show_list(self) -> None:
        if not self.products:
            print("Lista zakupów jest pusta.")
        else:
            print("Lista zakupów:")
            for product in self.products:
                print(product)
        

def main() -> None:
    terminal.clear()
    shopping_list = ShoppingList()
    
    while True:
        print("\nOpcje:")
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Edytuj produkt")
        print("4. Oznacz jako kupione / nie kupione")
        print("5. Pokaż listę zakupów")
        print("6. Wyjdź")
        
        choice: str = input("Wybierz opcję: ")
        
        if choice == '1':
            # ------------------------| ADD |------------------------
            terminal.clear()
            name = input("Podaj nazwę produktu: ")
            quantity = int(input("Podaj ilość: "))
            shopping_list.add_product(name, quantity)
        elif choice == '2':
            # ------------------------| REMOVE |------------------------
            terminal.clear()
            shopping_list.show_list()
            terminal.printSeperateLine()
            name = input("Podaj nazwę produktu do usunięcia: ")
            shopping_list.remove_product(name)
        elif choice == '3':
            # ------------------------| EDIT |------------------------
            terminal.clear()
            shopping_list.show_list()
            terminal.printSeperateLine()
            name = input("Podaj nazwę produktu do edycji: ")
            new_name = input("Podaj nową nazwę produktu: ")
            new_quantity = int(input("Podaj nową ilość: "))
            shopping_list.edit_product(name, new_name, new_quantity)
        elif choice == '4':
            # ------------------------| MARK |------------------------
            terminal.clear()
            shopping_list.show_list()
            terminal.printSeperateLine()
            name = input("Podaj nazwę produktu do oznaczenia jako kupione: ")
            shopping_list.mark_as_purchased(name)
        elif choice == '5':
            # ------------------------| SHOW |------------------------
            terminal.clear()
            shopping_list.show_list()
        elif choice == '6':
            # ------------------------| EXIT |------------------------
            break
        else:
            # ------------------------| DEFAULT |------------------------
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()
