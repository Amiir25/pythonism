#!/usr/bin/python3

"""
test_product.py

This module provides a unittest class for the
'product' module.
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def test_constructor(self):
        """Tests the constructor"""

        p1 = Product("B", 12.55, "Book", 21)
        self.assertEqual(p1.name, "B")
        self.assertEqual(p1.price, 12.55)
        self.assertEqual(p1.description, "Book")
        self.assertEqual(p1.stock, 21)
        self.assertEqual(p1, Product(name="B", price=12.55, description="Book", stock=21))


if __name__ == "__main__":
    unittest.main()
