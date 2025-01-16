# Enter your code here. Read input from STDIN. Print output to STDOUT
input_txt=input()
rows=int(input_txt.split()[0])
columns=int(input_txt.split()[1])

#Top cone
t_cone_rows=rows//2
n=1
for _ in range(t_cone_rows):
    pattern=".|."*n
    print(pattern.center(columns,'-'))
    n+=2
#Middle row
print("WELCOME".center(columns,'-'))

#Bottom Cone
n-=2
for _ in range(t_cone_rows):
    pattern=".|."*n
    print(pattern.center(columns,'-'))
    n-=2