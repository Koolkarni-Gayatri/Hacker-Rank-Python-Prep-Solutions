# Use the language Pypy3 instead of Python 3
if __name__=="__main__":
    n=int(input())
    tup_ele=input().split()
    tup_ints=[int(i) for i in tup_ele]
    my_tup=tuple(tup_ints)
    print(hash(my_tup))