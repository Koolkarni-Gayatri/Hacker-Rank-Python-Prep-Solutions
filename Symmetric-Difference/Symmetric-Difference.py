# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(m_arr, n_arr):
    first=set(m_arr)
    second=set(n_arr)
    inter_arr = first.intersection(second)
    union_arr=first.union(second)
    return sorted(union_arr.difference(inter_arr))
    
if __name__=='__main__':
    M=int(input())
    M_arr=list(map(int,input().split()))
    N=int(input())
    N_arr=list(map(int,input().split()))
    
    uncommon_list=symmetric_difference(M_arr,N_arr)
    for item in uncommon_list:
        print(item)