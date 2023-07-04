#!/usr/bin/python3
"""
101-lazy_matrix_mul module

This module contains lazy_matrix_mul() function

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns a new matrix where each element has been divided by div

    Args:
        m_a (list): list of lists of integers/floats
        m_b (list): list of lists of integers/floats
    """
    return np.dot(m_a, m_b)
