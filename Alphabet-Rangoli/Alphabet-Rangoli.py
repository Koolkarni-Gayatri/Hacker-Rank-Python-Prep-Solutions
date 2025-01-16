def print_rangoli(size):
    char_set="abcdefghijklmnopqrstuvwxyz"
    width=(4*size)-3
    # top cone
    for i in range(size-1,0,-1):
        pattern='-'.join(char_set[i:size])
        f_pattern=pattern[::-1]+pattern[1:]
        print(f_pattern.center(width,'-'))
    
    #Bottom Cone
    for i in range(size):
        pattern='-'.join(char_set[i:size])
        f_pattern=pattern[::-1]+pattern[1:]
        print(f_pattern.center(width,'-'))    
        
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)