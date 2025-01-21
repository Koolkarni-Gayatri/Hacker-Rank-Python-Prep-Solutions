# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoes_no=int(input())
sizes=input().split()
cust_count=int(input())
cust_pur=[]
for _ in range(cust_count):
    cust_pur.append(input())
int_sizes=[int(i) for i in sizes]
shelf=dict(Counter(int_sizes))
total_pur=0
for item in cust_pur:
    size=int(item.split()[0])
    price=int(item.split()[1])
    if size in int_sizes and shelf[size]>0:
        total_pur+=price
        shelf[size]-=1

print(total_pur)