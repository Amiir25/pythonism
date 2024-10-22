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

        return self.__price

    @price.setter
    def price(self, price):
        """Setter method for __price attribute"""

        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Invalid price! Price must be a positive number")

        self.__price = price

    @property
    def stock(self):
        """Getter method for __stock attribute"""

        return self.__stock

    @stock.setter
    def stock(self, stock):
        """Setter method for __stock attribute"""

        if not isinstance(stock, int) or stock < 0:
            raise Exception("Invalid stock! Stock must be a non-negative integer")

        self.__stock = stock
