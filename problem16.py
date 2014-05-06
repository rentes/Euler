"""Project Euler - Problem 16 - http://projecteuler.net/problem=16"""
import sys
import time
import math
import tools.timeutils as timeUtils


def main():
    """Main entry point for the script"""
    start = time.time()

    # short explanation:
    # str(number) - converts number to string
    # map(int,string) - converts each charater to int
    # sum(list) - sums the list of ints (in this case)
    print(sum(map(int, str(int(math.pow(2, 1000))))))

    timeUtils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
