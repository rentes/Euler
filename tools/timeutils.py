"""
Module for calculating and displaying the time an algorithm for
a given Euler problem took to run
"""

import time


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    hr = int(elapsed / 3600)  # hours
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', hr, 'hour,', min, 'min,', s, 's,', ms, 'ms')
