#!/usr/bin/python3

"""
test_product.py

This module provides a unittest class for the
'product' module.
"""

import unittest
from product import Product
import exceptions

class TestProduct(unittest.TestCase):

    def setUp(self):
        """This method runs before every test"""

        self.p1 = Product(".py", 12.55, "Python Book", 21)        

    def test_constructor(self):
        """Test the constructor"""

        self.assertEqual(self.p1.name, ".py")
        self.assertEqual(self.p1.price, 12.55)
        self.assertEqual(self.p1.description, "Python Book")
        self.assertEqual(self.p1.stock, 21)
        self.assertEqual(self.p1, Product(name=".py", price=12.55, description="Python Book", stock=21))


    def test_valid_price(self):
        """Test the 'price' attribute with valid data"""

        self.p1.price = 43
        self.assertEqual(self.p1.price, 43)
        self.p1.price = 123.4567
        self.assertEqual(self.p1.price, 123.4567)
        self.p1.price = 0.175
        self.assertEqual(self.p1.price, 0.175)

    def test_invalid_price(self):
        """Test the 'price' attribute with invalid data"""

        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = 0
        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = -21.55
        with self.assertRaises(exceptions.InvalidPriceError):
            self.p1.price = "21.55"

    def test_valid_stock(self):
        """Test the 'stock' attribute with valid data"""

        self.p1.stock = 127
        self.assertEqual(self.p1.stock, 127)
        self.p1.stock = 0
        self.assertEqual(self.p1.stock, 0)

    def test_invalid_stock(self):
        """Test the 'stock' attribute with invalid data"""

        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = -21
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = "21"
        with self.assertRaises(exceptions.InvalidStockError):
            self.p1.stock = 21.75

    def test_is_in_stock(self):
        """Test if a product is in stock"""

        self.p1.stock = 22
        self.assertEqual(self.p1.is_in_stock(), True)
        self.p1.stock = 0
        self.assertEqual(self.p1.is_in_stock(), False)

if __name__ == "__main__":
    unittest.main()
