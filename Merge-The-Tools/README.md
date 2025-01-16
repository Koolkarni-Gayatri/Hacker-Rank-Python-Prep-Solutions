# Merge the Tools

Consider the following:

- A string, s, of length n where s=c<sub>0</sub>c<sub>1</sub>c<sub>2</sub>.....c<sub>n-1</sub>.
- An integer, k, where k is a factor of n.

We can split s into $\frac{n}{k}$ substrings where each subtring, t<sub>i</sub>, consists of a contiguous block of k characters in s. Then, use each t<sub>i</sub> to create string u<sub>i</sub> such that:

- The characters in u<sub>i</sub> are a subsequence of the characters in t<sub>i</sub>.
- Any repeat occurrence of a character is removed from the string such that each character in u<sub>i</sub> occurs exactly once. In other words, if the character at some index j in t<sub>i</sub> occurs at a previous index \<j in t<sub>i</sub>, then do not include the character in string u<sub>i</sub>.

Given s and k, print $\frac{n}{k}$ lines where each line i denotes string u<sub>i</sub>.

#### Example
s='AAABCADDE'\
k=3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u<sub>1</sub>='A'. The second substring has all distinct characters, so u<sub>2</sub>='BCA'. The third substring has  different characters, so u<sub>3</sub>='DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

#### Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

- string s: the string to analyze
- int k: the size of substrings to analyze
  
Prints

Print each subsequence on a new line. There will be $\frac{n}{k}$ of them. No return value is expected.

## Input Format

The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

#### Constraints

- 1\<=n\<=10<sup>4</sup>, where n is the length of s
- 1\<=k\<=n
- It is guaranteed that n is a multiple of k.
## Sample Input
```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
```
## Sample Output
```
AB
CA
AD
```
## Explanation

Split s into $\frac{n}{k}=\frac{9}{3}$=3 equal parts of length k=3. Convert each t<sub>i</sub> to u<sub>i</sub> by removing any subsequent occurrences of non-distinct characters in t<sub>i</sub>:
1. t<sub>0</sub>="AAB" -> u<sub>0</sub>="AB"
2. t<sub>1</sub>="CAA" -> u<sub>1</sub>="CA"
3. t<sub>2</sub>="ADA" -> u<sub>2</sub>="AD"
Print each u<sub>i</sub> on a new line.
