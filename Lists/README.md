# Lists
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer _e_ at position _i_.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer _e_.
4. append e: Insert integer _e_ at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of _n_ followed by _n_ lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

**Example**\
_N=4_\
Append 1\
append 2\
insert 3 1\
print
- append 1: Append 1 to the list, _arr=\[1\]_.
- append 2: Append 2 to the list, _arr=\[1,2\]_.
- insert 3 1: Insert 3 at index 1, _arr=\[1,3,2\]_.
- print: Print the array.\
**Output:**
```
[1, 3, 2]
```
## Input Format

The first line contains an integer, _n_, denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

**Constraints**
- The elements added to the list must be integers.
## Output Format

For each command of type print, print the list on a new line.

**Sample Input 0**
```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```
**Sample Output 0**
```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```
