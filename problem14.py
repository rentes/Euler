"""Project Euler - Problem 14 - http://projecteuler.net/problem=14"""
import sys
import time
import tools.timeutils as timeutils


def collatz_sequence(n):
    """
    Returns a list with the Collatz sequence given n
    """
    collatz_sequence_list = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
            collatz_sequence_list.append(n)
        else:
            n = int(3 * n + 1)
            collatz_sequence_list.append(n)
    return collatz_sequence_list


def main():
    """Main entry point for the script"""
    start = time.time()

    longest_length = 0
    longest_number = 0
    number = 1000000

    while number > 1:
        collatz_sequence_length = len(collatz_sequence(number))
        if collatz_sequence_length > longest_length:
            longest_length = collatz_sequence_length
            longest_number = number
        number -= 1
    print(longest_number)

    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
