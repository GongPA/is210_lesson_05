#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_03:Transforming Data
"""

def celsius_to_fahrenheit(TEMPERATURE):
    #convert C to F
    FAHRENHEIT = (TEMPERATURE * 9) / 5 + 32
    return round(float(FAHRENHEIT),1)# only need 1 afetr decimal


def fahrenheit_to_celsius(TEMPERATURE):
    #convert F to C
    CELSIUS =(TEMPERATURE - 32)*5 / 9
    return round(float(CELSIUS),1) # only need 1 afetr decimal


def convert_temperature(TEMPERATURE, OUTPUT_FORMAT='c'):
    #function recall functions
    if isinstance(TEMPERATURE, basestring):
        TEMP = float(TEMPERATURE[0:-1])
        DEGREE_TYPE = TEMPERATURE[-1].lower()
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
