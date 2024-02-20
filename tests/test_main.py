#!/usr/bin/env python
# -*- coding: utf-8 -*-
from simple_calculator import SimpleCalculator

def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(5, 4)
    assert result == 9


