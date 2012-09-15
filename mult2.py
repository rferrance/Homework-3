# ECE 2524 Homework 3 Problem 2 Randall Ferrance

import sys
import fileinput
import argparse

parser = argparse.ArgumentParser(description='Positional arguements.')
parser.add_argument('infile', type=str,  nargs="*", default="-")
parser.add_argument('-b', '--ignore-blank', dest='ignoreblank', action='store_true', help='Ignore the blank lines')
parser.add_argument('-n', '--ignore-non-numeric', dest='ignorenonnumeric', action='store_true', help='Ignore non numeric characters')

args = parser.parse_args()

total = 1

for line in fileinput.input(args.infile):
    try:
        float(line)
    except ValueError as e:
        if (line=="\n"):
            formatTotal='{0:.3g}'.format(float(total))
            if args.ignoreblank:
                line = "1"
            else:
                print formatTotal
                line = "1"
        else:
            if(args.ignorenonnumeric):
                line = '1'
            else:
                sys.stderr.write(str(e))
                sys.exit(1)
    total *= float(line)
    
formatTotal='{0:.3g}'.format(float(total))
   
print(formatTotal)
    
