"""
Module: exception

This module contains custom exception classes
used for handling specific error scenarios in function module.
"""


class InvalidInput(Exception):
    """
    Exception raised when the input data is invalid or does not meet expectations.
    """


class InvalidLength(Exception):
    """
    Exception raised when the length of the data is invalid or does not meet expectations.
    """
