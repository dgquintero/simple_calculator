#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
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

def test_mul_two_numbers():
    """ test mul_two_numbers"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.mul(5, 4)

    assert result == 20 # first computes result == 20 -> boolean assert passed if is True otherwise raise exception if result is False

def test_mul_by_zero_raises_exception():
    """ test mul_by_zero_raises_exception"""
    calculator = SimpleCalculator() # instatiated the class calculator

    with pytest.raises(ValueError):
        calculator.mul(5, 0)

def test_div_two_numbers():
    """test division"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.div(5, 0)

    assert result == float('inf') # first computes result == 1.25 -> boolean assert passed if is True otherwise raise exception if result is False


# AVG TESTS
def test_avg_correct_average():
    """ test avg_correct_average"""
    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([2, 5, 12, 98])

    assert result == 29.25 # first computes result == 29.25 -> boolean assert passed if is True otherwise raise exception if result is False

def test_avg_upper_threshold():
    """Test upper threshold"""

    calculator = SimpleCalculator() # instatiated the class calculator with

    result = calculator.avg([2, 5, 12, 98], ut=90)

    assert result == pytest.approx(6.333333) # first computes result == 7.25 -> boolean assert passed if is True otherwise raise exception if result is False

def test_avg_lower_threshold():
    """Test lower threshold"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([2, 5, 12, 98], lt=10)

    assert result == 55 # first computes result == 55 -> boolean assert passed if is True otherwise raise exception if result is False

def test_avg_upper_and_lower_threshold():
    """Test upper and lower threshold"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([2, 5, 12, 98], lt=10, ut=90)

    assert result == 12

def test_avg_empty_list():
    """Test empty list"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([])

    assert result == 0 # first computes result == 0 -> boolean assert passed if is True otherwise raise exception if result is False

def test_avg_empty_list_with_thresholds():
    """Test empty list with thresholds"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([], lt=10, ut=90)

    assert result == 0 # first computes result == 0 -> boolean assert passed if is True otherwise raise exception if result is False

def test_avg_empty_list_after_thresholds():
    """Test lt and gt thresholds"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([2, 5, 12, 98], lt=15, ut=90)

    assert result == 0


def test_avg_manages_zero_value_lower_outlier():
    """Test lt and gt thresholds"""

    calculator = SimpleCalculator() # instatiated the class calculator

    result = calculator.avg([-1, 0, 1], lt=0)

    assert result == 0.5
    
