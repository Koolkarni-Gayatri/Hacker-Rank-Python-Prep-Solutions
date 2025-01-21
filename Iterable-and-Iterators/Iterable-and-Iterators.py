# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

nb, tot = 0, 0
for t in combinations([i for i in range(n)], k):
    tot += 1
    for i in t:
        if letters[i] == 'a':
            nb += 1
            break
print(round(nb / tot, 12))