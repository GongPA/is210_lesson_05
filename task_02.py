#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_02:Loan Calculator Revisited
"""

from decimal import Decimal

def get_interest_rate(principal, duration, prequalification):
    # Returns the interest rate
    RATE = 0
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                RATE = '0.0363'
            else:
                RATE = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                RATE = '0.0404'
            else:
                RATE = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                RATE = '0.0577'
            else:
                RATE = '0.0639'
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                RATE = '0.0302'
            else:
                RATE = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                RATE = '0.0327'
            else:
                RATE = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                RATE = '0.0466'
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                RATE = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                RATE = '0.0262'
    if RATE is not None:
        RATE = Decimal(RATE)
    return RATE


def compound_interest(principal, duration, rate, interval=12):
    # Returns the compound interest
    
    if RATE is not None:
        RATE = Decimal(RATE)
        return principal * ((1 + RATE / interval) ** (interval * duration))
    return None


def calculate_total(principal, duration, prequalification):
    # Returns the calculated TOTAL
    TOTAL=0
    INTERESTRATE = get_interest_rate(principal, duration, prequalification)
    if INTERESTRATE is not None:
        TOTAL = compound_interest(principal, duration, INTERESTRATE)
        return int(round(TOTAL))
    return None


def calculate_interest(principal, duration, prequalification):
    # Returns the calculated interest
    TOTAL=0
    INTERESTRATE = get_interest_rate(principal, duration, prequalification)
    TOTAL = compound_interest(principal, duration, INTERESTRATE)
    if INTERESTRATE is not None:
        return int(round(TOTAL - principal))
    return None
