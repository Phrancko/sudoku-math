# sudoku-math
Provides assistance with the simple math required for sudoku variant puzzles, like killer, arrow, sandwich, and others that involved finding digits 1-9 that add up to certain totals.

## What is this?

Sudoku variant puzzles are variations on the classic sudoku in which you have to arrange the digits 1 to 9 in a 9x9 grid which is divided into nine 3x3 boxes of 9 cells such that every row, every column and each 3x3 box contains the digits 1 to 9.

There are a large number of variants to the classic sudoku. They are explained and demonstrated on the terrific YouTube channel, Cracking the Cryptic. Many of the variants ask you to fill a number of cells with digits which add to a specific total.  Sometimes the number of digits is known but the total is not known (as in arrow sudokus and some killer sudokus) and sometimes both the number of digits is known and the total is known (more common killer sudokus). Sometimes one or more of the digits being summed are already known.

Sometimes the exact number of digits is not known but the total is known (sandwich sudokus). This version of the utility does not handle that case directly, though the information can be gleaned through multiple calls.

## Why did I write this?

In tackling sudoku variants I often found myself asking questions like:
1. What are all the ways four different digits can add up to 14 without repeating any digits?
2. I know I need 5 digits that add up to 14 and I know two of them are 5 and 6. What combinations are possible with no repeats?
3. What totals are possible given exactly five digits with no repeats?
4. If there are 3 different digits that add up to 8, how do I know one of the digits must be a 1?

I found myself spending far too much time trying to enumerate the possibilities in my head. So I wrote this little utility to give me quick answers. The answers to those questions are in the following outputs from the utility:

1. {14: [[1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 4, 6], [2, 3, 4, 5]]}
2. {24: [[1, 3, 5, 6, 9], [1, 4, 5, 6, 8], [2, 3, 5, 6, 8], [2, 4, 5, 6, 7]]}
3. [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
4. Yes! the only possibilities are {8: [[1, 2, 5], [1, 3, 4]]}

Note: Some variants allow muliple digits to have repeated digits in the numbers being summed. This utility does not help with those. It only works on totals made from non-repeating digits.

## Syntax

The primary command is the python file get_sums.py. If you call it with no arguments, it prints the following usage statement:
```
Usage: get_sums.py number_of_digits total [already_have]
where 
    - number_of_digits is an integer from 1 to 9
    - total is either 0 (default) or an appropriate number less than or equal to 45. If 0, then all possible totals are considered
    - already_have (optional) is a list of numbers already contributing to the total
```      
To get the answer to the first question above:
`./get_sums.py 4 14`
The second is answered by:
`./get_sums.py 5 14 5 6`
The third answer comes from:
`./get_sums.py 5`
And the fourth is given by:
`./get_sums.py 8`

## What are all these files?
- get_sums.py - the primary utility, reads the pickle file all_sums.pkl and uses the data to quickly produce the output
- create_sums.py - the program that generated all the possible answers as a dictionary whose keys are totals and whose values are the lists of non-repeating digits that produce that total. It then saved the data in the pickle file. The program takes a few minutes to run.
- all_sums.pkl - the pickle file that stores the result of create_sums.py
- sums.py - the module that contains the work horses for both create_sums.py and get_sums.py

## Who did this?
This module was created and is maintained by Frank H. Jernigan.

