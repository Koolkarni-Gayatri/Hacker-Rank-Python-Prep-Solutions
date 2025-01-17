# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
input_string=input().split()
string=input_string[0].upper()
substring_length=int(input_string[1])
permutes=list(permutations(string,substring_length))
str_permute=[]
for permute in permutes:
    l_str=""
    for i in permute:
        l_str+=i
    str_permute.append(l_str)
str_permute.sort()
[print(i) for i in str_permute]