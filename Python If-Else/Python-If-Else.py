#!/bin/python3

import math
import os
import random
import re
import sys

def weird(n):
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        elif n > 20:
            print("Not Weird")
        else:
            print("Number doesn't belong to above conditions")
    else:
        print("Number is greater than 100")

if __name__ == '__main__':
    n = int(input().strip())
    weird(n)