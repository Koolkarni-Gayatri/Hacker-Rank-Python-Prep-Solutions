# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    operation, _ = input().split()
    other_set=set(map(int,input().split()))
    eval(f"A.{operation}({other_set})")

print(sum(A))