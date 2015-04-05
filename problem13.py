"""Project Euler - Problem 13 - http://projecteuler.net/problem=13"""
import sys
import time
import tools.timeutils as timeutils


def main():
    """Main entry point for the script"""
    start = time.time()
    a = 0
    with open('problem13-data.txt') as f:
        for line in f:
            b = int(line.strip())
            a += b
    print(str(a)[:10])
    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
