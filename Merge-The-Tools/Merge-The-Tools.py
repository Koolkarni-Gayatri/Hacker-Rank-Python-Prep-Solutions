def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sub_str=string[i:i+k]
        l_sub=list(sub_str)
        u_lst=[]
        [u_lst.append(i) for i in l_sub if i not in u_lst]
        print("".join(u_lst))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)