"""Project Euler - Problem 13 - http://projecteuler.net/problem=13"""
import sys
import time
import tools.timeutils as timeUtils


def collatz_sequence(n):
    """
    Returns a list with the Collatz sequence given n
    """
    collatz_sequence = []
    collatz_sequence.append(n)
    while (n > 1):
        if n % 2 == 0:
            n = int(n / 2)
            collatz_sequence.append(n)
        else:
            n = int(3 * n + 1)
            collatz_sequence.append(n)
    return collatz_sequence


def main():
    """Main entry point for the script"""
    start = time.time()
    longest_length = 0
    collatz_sequence_length = 0
    longest_number = 0
    number = 1000000
    while number > 1:
        collatz_sequence_length = len(collatz_sequence(number))
        if collatz_sequence_length > longest_length:
            longest_length = collatz_sequence_length
            longest_number = number
        number -= 1
    print(longest_number)
    timeUtils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
