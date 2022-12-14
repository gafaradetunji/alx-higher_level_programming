#!/usr/bin/bash

""" Defines a Rectangle Class """


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Defines  a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """setter of private instance width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private instance width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter of private instance height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of private instance height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
