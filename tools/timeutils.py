"""
Simple module for calculating and displaying the time an algorithm for
a given Euler problem took to run
Author: Miguel Rentes
"""


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    hours = int(elapsed / 3600)  # hours
    minutes = int((elapsed % 3600) / 60)  # minutes
    seconds = int(elapsed) % 60  # seconds
    milliseconds = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', hours, 'hour,', minutes, 'min,', seconds, 's,', milliseconds, 'ms')
