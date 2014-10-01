#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task_02:Loan Calculator Revisited
"""


from decimal import Decimal


def get_interest_rate(principal, duration, prequalification):
    """Returns the interest rate"""
    rate = None
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0466'
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0262'
    if rate is not None:
        rate = Decimal(rate)
    return rate


def compound_interest(principal, duration, rate, interval=12):
    """Returns the compound interest"""
    if rate is not None:
        rate = Decimal(rate)
        return principal * ((1 + rate / interval) ** (interval * duration))
    return None


def calculate_total(principal, duration, prequalification):
    """Returns the calculated TOTAL"""
    total = 0
    interestrate = get_interest_rate(principal, duration, prequalification)
    if interestrate is not None:
        total = compound_interest(principal, duration, INTERESTrate)
        return int(round(total))
    return None


def calculate_interest(principal, duration, prequalification):
    """Returns the calculated interest"""
    total = 0
    interestrate = get_interest_rate(principal, duration, prequalification)
    total = compound_interest(principal, duration, INTERESTrate)
    if interestrate is not None:
        return int(round(total - principal))
    return None
