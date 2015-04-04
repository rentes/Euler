"""Project Euler - Problem 4 - http://projecteuler.net/problem=4"""
import sys
import math
import time
import tools.timeutils as timeUtils


def number_of_digits(n):
    """
    Returns the number of digits an integer has
    Returns: int
    """
    return 1 + int(math.log10(n))


def is_palindrome(n):
    otherwise_ = """
    Finds if a given n is a palindrome
    Returns: bool (True if a palindrome, False otherwise)
    """
    nr_digits = number_of_digits(n)
    if nr_digits == 1:
        return True
    elif nr_digits == 2:
        if int(n / 10) == n % 10:
            return True
        else:
            return False
    elif nr_digits == 3:
        if int(n / 100) == (n % 100) % 10:
            return True
        else:
            return False
    elif nr_digits == 4:
        if int(n / 1000) == ((n % 1000) % 100) % 10 and \
           int((n % 1000) / 100) == int(((n % 1000) % 100) / 10):
            return True
        else:
            return False
    elif nr_digits == 5:
        if int(n / 10000) == (((n % 10000) % 1000) % 100) % 10 and \
           int((n % 10000) / 1000) == int((((n % 10000) % 1000) % 100) / 10):
            return True
        else:
            return False
    elif nr_digits == 6:
        if int(n / 100000) == ((((n % 100000) % 10000) % 1000) % 100) % 10 \
           and int((n % 100000) / 10000) == \
           int(((((n % 100000) % 10000) % 1000) % 100) / 10) \
           and int(((n % 100000) % 10000) / 1000) == \
           int((((n % 100000) % 10000) % 1000) / 100):
            return True
        else:
            return False
    else:
        print('Number of digits higher than 6. Pass.')
        return False


def largest_palindrome():
    """
    Finds the largest palindrome made from the product of two 3-digit numbers
    """
    # numbers for product
    number1, number2 = 1, 2
    # to record last found largest palindrome
    largest_palindrome = 0
    while number1 < 1000:
        while number2 < 1000:
            product = number1 * number2
            if is_palindrome(product):
                if product > largest_palindrome:
                    # update largest palindrome
                    largest_palindrome = product
            number2 += 1
        # reset number2
        number2 = 2
        number1 += 1
    print('largest palindrome is', largest_palindrome)


def main():
    """Main entry point for the script"""
    start = time.time()
    largest_palindrome()
    timeUtils.elapsed_time(time.time() - start)


if __name__ == '__main__':
    sys.exit(main())
