#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 01: Defining a Function
"""


def bool_to_str(bvalue, short=False):
    """convert bool to string"""
    if bvalue is True:
        if not short:
            return 'Yes'
        else:
            return 'Y'
    elif bvalue is False:
        if not short:
            return 'No'
        else:
            return 'N'
