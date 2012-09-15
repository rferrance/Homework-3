# ECE 2524 Homework 3 Problem 1 Randall Ferrance

import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
args = parser.parse_args()


total = 1;


for line in iter(sys.stdin.readline,""):
    try:
        float(line)
    except ValueError as e:
        if (line=="\n"):
            formatTotal='{0:.3g}'.format(float(total))
            print formatTotal
            line = "1"
        else:
            sys.stderr.write(str(e))
            sys.exit(1)
    total *= float(line)
    
formatTotal='{0:.3g}'.format(float(total))
   
print(formatTotal)
    

    
            



