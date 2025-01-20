# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

input_string=input().split()
word=input_string[0].upper()
number=int(input_string[1])

combinations=list(combinations_with_replacement(word,number))
display=[]
for combination in combinations:
    tup=sorted(combination)
    str_join="".join(list(tup))
    display.append(str_join)

display.sort()
[print(i) for i in display]