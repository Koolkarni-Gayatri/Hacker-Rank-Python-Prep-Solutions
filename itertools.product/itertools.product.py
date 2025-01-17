# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

r1=input().split()
r2=input().split()
l1=[int(i) for i in r1]
l2=[int(i) for i in r2]
p_list=list(product(l1,l2))
for i in p_list:
    print(i,end=" ")