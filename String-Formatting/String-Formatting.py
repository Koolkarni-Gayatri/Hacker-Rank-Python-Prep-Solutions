def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        d_txt="{0:d}"
        o_txt="{0:o}"
        h_txt="{0:X}"
        b_txt="{0:b}"
        print(d_txt.format(i).rjust(width),o_txt.format(i).rjust(width),h_txt.format(i).rjust(width),b_txt.format(i).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)