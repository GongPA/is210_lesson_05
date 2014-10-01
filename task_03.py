#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_03:Transforming Data
"""


def celsius_to_fahrenheit(temperature):
    """convert C to F"""
    fahrenheit = (temperature * 9) / 5 + 32
    return round(float(fahrenheit), 1)  # only need 1 afetr decimal


def fahrenheit_to_celsius(temperature):
    """ convert F to C"""
    celsius = (temperature - 32)*5 / 9
    return round(float(celsius), 1)  # only need 1 afetr decimal


def convert_temperature(temperature, output_format='c'):
    """ Function recall functions"""
    temp = None
    degree_type = None
    
    if isinstance(temperature, basestring):
        temp = float(temperature[0:-1])
        degree_type = temperature[-1].lower()
    else:
        return None

    if output_format == 'f':
        if degree_type == 'c':
            return celsius_to_fahrenheit(temp)
        elif degree_type == 'f':
            return temp
        else:
            return None
    elif output_format == 'c':
        if degree_type == 'f':
            return fahrenheit_to_celsius(temp)
        elif degree_type == 'c':
            return temp
        else:
            return None
