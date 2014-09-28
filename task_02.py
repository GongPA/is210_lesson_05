#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_02:Loan Calculator Revisited
"""

from decimal import Decimal

def get_interest_rate(PRINCIPAL, DURATION, PREQUALIFICATION):
    #Returns the interest rate
    RATE = None
    if PRINCIPAL >= 0 and PRINCIPAL <= 199999:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0363'
            else:
                RATE = '0.0465'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0404'
            else:
                RATE = '0.0498'
        elif DURATION >= 21 and DURATION <= 30:
            if PREQUALIFICATION:
                RATE = '0.0577'
            else:
                RATE = '0.0639'
    elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0302'
            else:
                RATE = '0.0398'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0327'
            else:
                RATE = '0.0408'
        elif DURATION >= 21 and DURATION <= 30:
            if PREQUALIFICATION:
                RATE = '0.0466'
    elif PRINCIPAL >= 1000000:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0205'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0262'
    if RATE is not None:
        RATE = Decimal(RATE)
    return RATE


def compound_interest(PRINCIPAL, DURATION, RATE, INTERVAL=12):
    #Returns the compound interest
    
    if RATE is not None:
        RATE = Decimal(RATE)
        return PRINCIPAL * ((1 + RATE / INTERVAL) ** (INTERVAL * DURATION))
    return None


def calculate_total(PRINCIPAL, DURATION, PREQUALIFICATION):
    #Returns the calculated TOTAL
    
    INTERESTRATE = get_interest_rate(PRINCIPAL, DURATION, PREQUALIFICATION)
    if INTERESTRATE is not None:
        TOTAL = compound_interest(PRINCIPAL, DURATION, INTERESTRATE)
        return int(round(TOTAL))
    return None


def calculate_interest(PRINCIPAL, DURATION, PREQUALIFICATION):
    #eturns the calculated interest
    
    INTERESTRATE = get_interest_rate(PRINCIPAL, DURATION, PREQUALIFICATION)
    TOTAL = compound_interest(PRINCIPAL, DURATION, INTERESTRATE)
    if INTERESTRATE is not None:
        return int(round(TOTAL - PRINCIPAL))
    return None
