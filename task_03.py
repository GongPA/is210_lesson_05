#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_03:Transforming Data
"""


def celsius_to_fahrenheit(temperature):
    """convert C to F"""
FAHRENHEIT = (temperature * 9) / 5 + 32
return round(float(FAHRENHEIT), 1)  # only need 1 afetr decimal


def fahrenheit_to_celsius(temperature):
    """ convert F to C"""
CELSIUS = (temperature - 32)*5 / 9
return round(float(CELSIUS), 1)  # only need 1 afetr decimal


def convert_temperature(temperature, output_format='c'):
    """ Function recall functions"""
if isinstance(temperature, basestring):
    TEMP = float(temperature[0:-1])
    DEGREE_TYPE = temperature[-1].lower()
else:
    return None

if OUTPUT_FORMAT == 'f':
    if DEGREE_TYPE == 'c':
        return celsius_to_fahrenheit(TEMP)
    elif DEGREE_TYPE == 'f':
        return TEMP
    else:
        return None
    elif OUTPUT_FORMAT == 'c':
        if DEGREE_TYPE == 'f':
            return fahrenheit_to_celsius(TEMP)
        elif DEGREE_TYPE == 'c':
            return TEMP
    else:
        return None
