# Text Wrap

You are given a string _S_ and width _w_.
Your task is to wrap the string into a paragraph of width _w_.

#### Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

- string string: a long string
- int max_width: the width to wrap to
#### Returns

- string: a single string with newline characters ('\n') where the breaks should be
## Input Format

The first line contains a string, _string_.
The second line contains the width, _maxwidth_.

#### Constraints
- 0\<_len\(string\)_\<1000
- 0\<maxwidth\<_len\(string\)_
## Sample Input 0
```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```
## Sample Output 0
```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```
