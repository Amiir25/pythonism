#!/usr/bin/python3

"""
test_product.py

This module provides a unittest class for the 'product' module.
"""

import unittest
import exceptions
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """This method runs before every test"""

        self.p1 = Product(".py", 12.55, "Python Book", 21)

    def test_constructor(self):
        """Test the __init__ constructor"""

        self.assertEqual(self.p1.name, ".py")
        self.assertEqual(self.p1.price, 12.55)
        self.assertEqual(self.p1.description, "Python Book")
        self.assertEqual(self.p1.stock, 21)

        self.assertEqual(self.p1, Product(
            name=".py", price=12.55, description="Python Book", stock=21))

    def test_valid_price(self):
        """Test the 'price' attribute with valid input"""

        self.p1.price = 43
        self.assertEqual(self.p1.price, 43)
        self.p1.price = 123.4567
        self.assertEqual(self.p1.price, 123.4567)
        self.p1.price = 0.175
        self.assertEqual(self.p1.price, 0.175)

    def test_invalid_price(self):
        """Test the 'price' attribute with invalid input"""

        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = 0
        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = -21.55
        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = "21.55"

    def test_valid_stock(self):
        """Test the 'stock' attribute with valid input"""

        self.p1.stock = 127
        self.assertEqual(self.p1.stock, 127)
        self.p1.stock = 0
        self.assertEqual(self.p1.stock, 0)

    def test_invalid_stock(self):
        """Test the 'stock' attribute with invalid input"""

        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = -21
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = "21"
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = 21.75

    def test_is_in_stock(self):
        """Test if a product is in stock"""

        self.assertEqual(self.p1.is_in_stock(), True)
        self.p1.stock = 0
        self.assertEqual(self.p1.is_in_stock(), False)

    def test_add_stock(self):
        """Test if the class adds stock correctly"""

        self.p1.add_stock(10)
        self.assertEqual(self.p1.stock, 31)
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.add_stock(0)
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.add_stock(-10)

    def test_remove_stock(self):
        """Test if the class removes stock correctly"""

        self.p1.remove_stock(10)
        self.assertEqual(self.p1.stock, 11)
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.remove_stock(0)
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.remove_stock(100)
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.remove_stock(-10)


if __name__ == "__main__":
    unittest.main()
