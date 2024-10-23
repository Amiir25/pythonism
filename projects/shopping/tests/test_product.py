#!/usr/bin/python3

"""
test_product.py

A Unit test file
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def test_constructor(self):
        """Tests the constructor"""

        p1 = Product("Book", 12.55, "Educational Book", 21)
        self.assertEqual(p1, Product(name=Book, price=12.55, stock=21))


if __name__ == "__main__":
    unittest.main()
