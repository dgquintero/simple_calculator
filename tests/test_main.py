#!/usr/bin/env python
# -*- coding: utf-8 -*-
from simple_calculator.main import SimpleCalculator # simplecalculator class is
# imported from simple_calculator.py

def test_add_two_numbers():
    """ test add_two_numbers"""
    calculator = SimpleCalculator() # instatiated the class
    result = calculator.add(5, 4)
    assert result == 9 # first computes result == 9 -> boolean assert passed if is True otherwise raise exception if result is False

def test_add_three_numbers():
    """ test add_three_numbers"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.add(4, 5, 6)

    assert result == 15# first computes result == 15 -> boolean assert passed if is True otherwise raise exception if result is False

def test_add_multiple_numbers():
    """ test add_multiple_numbers"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.add(1, 2, 3, 4, 5)

    assert result == 15 # first computes result == 15 -> boolean assert passed if is True otherwise raise exception if result is False

def test_substact_two_numbers():
    """ test substact_two_numbers"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.substract(5, 4)

    assert result == 1 # first computes result == 1 -> boolean assert passed if is True otherwise raise exception if result is False

