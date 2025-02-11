# Polar coordinates

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number 

z=x + yj

is completely determined by its real part x and imaginary part y.

Here, j is the imaginary unit.
A polar coordinate (r, Φ) 
![Polar Coordinates](https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG)

is completely determined by modulus r and phase angle Φ.

If we convert complex number z to its polar coordinate, we find:
- r: Distance from z to origin, i.e., $`\sqrt{x^2+y^2}`$ 
- Φ: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.

_cmath.phase_

This tool returns the phase of complex number z (also known as the argument of z).
```
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
````
_abs_
This tool returns the modulus (absolute value) of complex number z.
```
>>> abs(complex(-1.0, 0.0))
1.0
```
## Task
You are given a complex z. Your task is to convert it to polar coordinates.

## Input Format

A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

#### Constraints

Given number is a valid complex number

## Output Format

Output two lines:
The first line should contain the value of r.
The second line should contain the value of Φ.

## Sample Input
```
  1+2j
```
## Sample Output
```
 2.23606797749979 
 1.1071487177940904
```
__Note:__ The output should be correct up to 3 decimal places.
