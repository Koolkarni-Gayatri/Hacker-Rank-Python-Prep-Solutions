# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
input_list=input().split()
string=input_list[0].upper()
com_len=int(input_list[1])
f_Arr=[]
for i in range(1,com_len+1):
    total=[]
    combs=list(combinations(string,i))
    for comb in combs:
        sorted_comb=sorted(comb)
        s_str=""
        for s_comb in sorted_comb:
            s_str+=s_comb
        total.append(s_str)
    total.sort()
    f_Arr+=total
[print(i) for i in f_Arr]