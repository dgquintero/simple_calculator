# -*- coding: utf-8 -*-

class SimpleCalculator:
    """ SimpleCalculator class"""
    def add(self, *args):
        """ add method"""
        return sum(args) # sum function returns the sum of all the elements in a list

    def substract(self, a, b):
        """ substract method"""
        return a - b
