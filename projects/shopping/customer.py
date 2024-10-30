#!/usr/bin/env python3

"""
customer.py

This file provides a 'Customer' class that contains information
about the customer.
"""

from product import Product
import exceptions


class Customer(Product):
    """The Customer class"""

    def __init__(self, name, email, address, order_history):
        """
        Instantiates attributes of Customer class.

        name (str): The name of the customer
        email (str): E-mail of the customer
        address (str): Address of the customer
        order_history (str): Order history of the customer
        """

        self.name = name
        self.email = email
        self.address = address
        self.order_history = order_history

    def __repr__(self):
        """Returns a representation of an object"""

        return "Customer(name={}, email={}, address={}, order_history={})".format(
            self.name, self.email, self.address, self.order_history)

    # Getter and Setter for email attribute
    @property
    def email(self):
        """Getter for __email attribute"""

        return self.__email

    @email.setter
    def email(self, email):
        """Setter for __email attribute"""

        if not isinstance(email, str):
            raise exceptions.InvalidEmailError(
                "Invalid Email! Must be a string")

        if '@' or '.' not in email:
            raise exceptions.InvalidEmailError(
                "Email must contain @ and . signs")

        self.__email = email
