# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
input_string=input()

for k,c in groupby(input_string):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')