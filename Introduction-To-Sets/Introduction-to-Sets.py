def average(array):
    dist_arr=set(array)
    set_len=len(dist_arr)
    sum_arr=0
    for i in dist_arr:
        sum_arr+=i
    return sum_arr/set_len

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)