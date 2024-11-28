# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
rooms=list(map(int, input().split()))

total_sum=sum(rooms)

unique_sum=sum(set(rooms))
captain_room=(unique_sum*k -total_sum) // (k-1)

print(captain_room)
