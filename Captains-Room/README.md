# Captain's Room

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:\
→ A Captain.\
→ An unknown group of families consisting of _K_ members per group where _K_ ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear _K_ times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of _K_ and the room number list.

## Input Format

The first line consists of an integer, _K_, the size of each group.
The second line contains the unordered elements of the room number list.

**Constraints**\
1\<_K_\<1000

## Output Format
Output the Captain's room number.

**Sample Input**
```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```
**Sample Output**
```
8
```
## Explanation
The list of room numbers contains 31 elements. Since _K_ is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
Hence, 8 is the Captain's room number.
