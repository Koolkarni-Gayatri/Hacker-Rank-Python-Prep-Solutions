# Power - Mod Power
So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function _a^b_ as shown below:
```
>>> pow(a,b)
``` 
or
```
>>> a**b
```
It's also possible to calculate a^b mod m.
```
>>> pow(a,b,m)
```
This is very helpful in computations where you have to print the resultant % mod.

**Note**: Here, _a_ and _b_ can be floats or negatives, but, if a third argument is present, _b_ cannot be negative.

**Note**: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().

## Task
You are given three integers: _a_, _b_, and _m_. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

## Input Format
The first line contains _a_, the second line contains _b_, and the third line contains _m_.

**Constraints**\
1\<=_a_\<=10\
1\<=_b_\<=10\
1\<=_m_\<=1000
## Sample Input
```
3
4
5
```
## Sample Output
```
81
1
```
