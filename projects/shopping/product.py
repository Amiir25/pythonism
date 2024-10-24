#!usr/bin/env python3

"""
product.py

This file provides a Product class
"""

import exceptions


class Product:
    """The product class"""

    def __init__(self, name, price, description, stock):
        """
        Instantiates attributes of Product class

        Args:
            name (string): The name of the product
            price (float): The price of the product
            description (string): A description about the product
            stock (integer): stock quantity
        """

        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __repr__(self):
        """Returns a developer-friendly representation of an object"""

        return "Product(name={}, price={}, description={}, stock={})".format(
                self.name, self.price, self.description, self.stock)

    def __eq__(self, other):
        """ """

        if isinstance(other, Product):
            return (
                self.name == other.name and
                self.price == other.price and
                self.description == other.description and
                self.stock == other.stock
            )

        return False

    @property
    def price(self):
        """Getter method for __price attribute"""

        return self.__price

    @price.setter
    def price(self, price):
        """Setter method for __price attribute"""

        if not isinstance(price, (int, float)) or price <= 0:
            raise exceptions.InvalidPriceError(
               "Invalid price! Must be a positive number")

        self.__price = price

    @property
    def stock(self):
        """Getter method for __stock attribute"""

        return self.__stock

    @stock.setter
    def stock(self, stock):
        """Setter method for __stock attribute"""

        if not isinstance(stock, int) or stock < 0:
            raise exceptions.InvalidStockError(
                "Invalid stock! Must be a non-negative integer")

        self.__stock = stock

    def is_in_stock(self):
        """Checks if the product is in stock"""

        return self.stock > 0

    def add_stock(self, amount):
        """Adds a stock for a product"""

        if amount <= 0:
            raise exceptions.InvalidStockError(
                "Amount to add must be greater than 0")

        self.stock += amount

    def remove_stock(self, amount):
        """Removes a stock for a product"""

        if amount <= 0:
            raise exceptions.InvalidStockError(
                "Amount to remove must be greater than 0")

        if amount > self.stock:
            raise exceptions.InvalidStockError(
                "Can not remove more stock than available")

        self.stock -= amount
