# List Comprehension
Let's learn about list comprehensions! You are given three integers _x_, _y_ and _z_ representing the dimensions of a cuboid along with an integer _n_. 
Print a list of all possible coordinates given by (_i_,_j_,_k_) on a 3D grid where the sum of _i_+_j_+_k_ is not equal to _n_. 
Here, 0<=_i_<=_x_; 0<=_j_<=_y_; 0<=_k_<=_z_. Please use list comprehensions rather than multiple loops, as a learning exercise.

## Example
_x_=1
_y_=1
_z_=2
_n_=3

All permutations of \[_i_,_j_,_k_\] are:
\[\[0,0,0\],\[0,0,1\],\[0,0,2\],\[0,1,0\],\[0,1,1\],\[0,1,2\],\[1,0,0\],\[1,0,1\],\[1,0,2\],\[1,1,0\],\[1,1,1\],\[1,1,2\]\]

Print an array of the elements that do not sum to .
\[\[0,0,0\],\[0,0,1\],\[0,0,2\],\[0,1,0\],\[0,1,1\],\[1,0,0\],\[1,0,1\],\[1,1,0\],\[1,1,2\]\]

## Input Format

Four integers _x_,_y_,_z_ and _n_, each on a separate line.

**Constraints**

Print the list in lexicographic increasing order.

## Sample Input 0
```
1
1
1
2
```
## Sample Output 0
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

## Explanation 0

Each variable _x_,_y_ and _z_ will have values of 0 or 1. All permutations of lists in the form .
\[_i_,_j_,_k_\]=\[\[0,0,0\],\[0,0,1\],\[0,1,0\],\[0,1,1\],\[1,0,0\],\[1,0,1\],\[1,1,0\],\[1,1,1\]\]
Remove all arrays that sum to _n_=2 to leave only the valid permutations.

## Sample Input 1
```
2
2
2
2
```

## Sample Output 1
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```