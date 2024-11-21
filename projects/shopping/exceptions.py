#!/usr/bin/env python3

"""
exceptions.py

This module contains custom exception classes for the shopping project
"""


class InvalidPriceError(Exception):
    """Custom exception class for invalid price"""

    pass


class InvalidStockError(Exception):
    """Custom exception class for invalid stock"""

    pass

class InvalidEmailError(Exception):
    """Custome exception class for invalid email"""

    pass
