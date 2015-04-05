"""Project Euler - Problem 17 - http://projecteuler.net/problem=17"""
import sys
import time
import tools.timeutils as timeutils

string = ""


def count_thousands(n):
    """Appends the number to the thousands"""
    global string
    count_units(int(n / 1000))
    string += "thousand "
    count_hundreds(int(n % 1000))


def count_hundreds(n):
    """Appends the number to the hundreds"""
    global string
    count_units(int(n / 100))
    if n != 0:
        string += "hundred "
    if int(n % 100) != 0:
        string += "and "
    count_dozens(int(n % 100))


def count_dozens(n):
    """Appends the number to the dozens"""
    global string
    if n == 10:
        string += "ten "
    elif n == 11:
        string += "eleven "
    elif n == 12:
        string += "twelve "
    elif n == 13:
        string += "thirteen "
    elif n == 14:
        string += "fourteen "
    elif n == 15:
        string += "fifteen "
    elif n == 16:
        string += "sixteen "
    elif n == 17:
        string += "seventeen "
    elif n == 18:
        string += "eighteen "
    elif n == 19:
        string += "nineteen "
    else:
        if int(n / 10) == 2:
            string += "twenty "
        if int(n / 10) == 3:
            string += "thirty "
        if int(n / 10) == 4:
            string += "forty "
        if int(n / 10) == 5:
            string += "fifty "
        if int(n / 10) == 6:
            string += "sixty "
        if int(n / 10) == 7:
            string += "seventy "
        if int(n / 10) == 8:
            string += "eighty "
        if int(n / 10) == 9:
            string += "ninety "
        count_units(int(n % 10))


def count_units(n):
    """Appends the number to the units"""
    global string
    if n == 9:
        string += "nine "
    elif n == 8:
        string += "eight "
    elif n == 7:
        string += "seven "
    elif n == 6:
        string += "six "
    elif n == 5:
        string += "five "
    elif n == 4:
        string += "four "
    elif n == 3:
        string += "three "
    elif n == 2:
        string += "two "
    elif n == 1:
        string += "one "
    else:
        string += ""


def count_words(n):
    """
    Appends the number to the global string
    and counts the letters it takes for number n
    """
    if int(n / 1000) != 0:
        count_thousands(n)
    elif int(n / 100) != 0:
        count_hundreds(n)
    elif int(n / 10) != 0:
        count_dozens(n)
    else:
        count_units(n)


def main():
    """Main entry point for the script"""
    start = time.time()

    number = 1000

    while number >= 1:
        count_words(number)
        number -= 1

    # uncomment next line to view the string
    # print(string)

    # spaces don't count
    print(len(string.replace(" ", "")))

    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
