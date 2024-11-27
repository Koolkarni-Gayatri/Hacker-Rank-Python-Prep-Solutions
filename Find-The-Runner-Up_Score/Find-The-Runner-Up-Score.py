if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l_arr=list(set(arr))
    l_arr.sort(reverse=True)
    print(l_arr[1])
