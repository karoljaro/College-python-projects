import unittest
from main import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList()
        self.shopping_list.add_product("Jabłka", 5)
        self.shopping_list.add_product("Banany", 3)

    def test_add_product(self):
        self.shopping_list.add_product("Gruszki", 4)
        self.assertEqual(len(self.shopping_list.products), 3)
        self.assertEqual(self.shopping_list.products[-1].name, "Gruszki")
        self.assertEqual(self.shopping_list.products[-1].quantity, 4)

    def test_remove_product(self):
        self.shopping_list.remove_product("Jabłka")
        self.assertEqual(len(self.shopping_list.products), 1)
        self.assertEqual(self.shopping_list.products[0].name, "Banany")

    def test_edit_product(self):
        self.shopping_list.edit_product("Banany", "Pomarańcze", 7)
        self.assertEqual(self.shopping_list.products[1].name, "Pomarańcze")
        self.assertEqual(self.shopping_list.products[1].quantity, 7)

    def test_mark_as_purchased(self):
        self.shopping_list.mark_as_purchased("Banany")
        self.assertTrue(self.shopping_list.products[1].purchased)

    def test_show_list(self):
        try:
            self.shopping_list.show_list()
        except Exception as e:
            self.fail(f"show_list method raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
