#!usr/bin/env python3

"""
product.py

This file provides a Product class
"""


class Product:
    """The product class"""

    def __init__(self, name, price, description, stock):
        """Instantiates attributes of Product class"""

        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    @property
    def price(self):
        """Getter method for __price attribute"""

        return self.price

    @price.setter
    def price(self, price):
        """Setter method for __price attribute"""

        if price <= 0 or price not int:
            raise Exception("Invalid price")

        self.__price = price

    @property
    def stock(self):
        """Getter method for __stock attribute"""

        return self.stock

    @stock.setter
    def stock(self, stock):
        """Setter method for __stock attribute"""

        if stock <= 0 or stock not in int:
            raise Exception("Invalid stock")

        self.__stock = stock
