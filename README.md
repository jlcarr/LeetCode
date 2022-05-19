# LeetCode
Solutions to LeetCode problems in Python3

## Results
### Problem 1
- **Name**: Two Sum
- **Runtime**: 84 ms
- **Memory**: 16 MB
- **Solution**: Pop from the string front, add unless the next numeral is higher, in which case subtract.

### Problem 2
- **Name**: Add Two Numbers
- **Runtime**: 116 ms
- **Memory**: 14 MB
- **Solution**: Long addition using a carry, and using the original linked-lists as output in-place.

### Problem 3
- **Name**: Longest Substring Without Repeating Characters
- **Runtime**: 67 ms
- **Memory**: 14.1 MB
- **Solution**: Keep track of previous positions in a dict, keep track of the start of current duplicate-free string candidate.

### Problem 4
- **Name**: Median of Two Sorted Arrays
- **Runtime**: 159 ms
- **Memory**: 14.1 MB
- **Solution**: Modified binary search one one array, checking the complement pointer in the other array to see if the median is reached. Watch out for edge-cases and off-by-1 errors.

### Problem 5
- **Name**: Longest Palindromic Substring
- **Runtime**: 4052 ms
- **Memory**: 13.9 MB
- **Solution**: Because input size is small, just brute-forced checked for palindromes around each character.

### Problem 6
- **Name**: Zigzag Conversion
- **Runtime**: 70 ms
- **Memory**: 14.2 MB
- **Solution**: A closed form formula for the position of a character in the zig-zag grid can be made with modular arithmetic, after that it's a matter of sorting.

### Problem 7
- **Name**: Reverse Integer
- **Runtime**: 39 ms
- **Memory**: 14 MB
- **Solution**: Use modular arithmetic to chop down the number, checking for overflows by moving subtractions and dividions across the inequality.

### Problem 8
- **Name**: String to Integer (atoi)
- **Runtime**: 81 ms
- **Memory**: 13.9 MB
- **Solution**: Used regex to match the description and get the capture groups, after which manual clamping was applied.

### Problem 9
- **Name**: Palindrome Number
- **Runtime**: 84 ms
- **Memory**: 13.9 MB	
- **Solution**: Converted to string and compared with reverse.

### Problem 10
- **Name**: Regular Expression Matching
- **Runtime**: 60 ms
- **Memory**: 14.4 MB	
- **Solution**: Dynamic programming to run through the string and regex checking if they're still matching at each junction.

### Problem 11
- **Name**: Container With Most Water
- **Runtime**: 1077 ms
- **Memory**: 27.5 MB	
- **Solution**: 2 pointers meeting in the middle, incrementing the one of lowest height to break the bound.

### Problem 12
- **Name**: Integer to Roman
- **Runtime**: 44 ms
- **Memory**: 13.9 MB	
- **Solution**: Kept a sorted list of Roman numberal conversions, and used modular arithmetic to cut down the number incrementally.

### Problem 13
- **Name**: Roman to Integer
- **Runtime**: 66 ms
- **Memory**: 14 MB
- **Solution**: Pop from the string front, add unless the next numeral is higher, in which case subtract.

### Problem 14
- **Name**: Longest Common Prefix
- **Runtime**: 44 ms
- **Memory**: 13.8 MB
- **Solution**: Run through the candidate prefix on each iteration, stoping when a mismatch is found and only keeping the match.

### Problem 15
- **Name**: 3Sum
- **Runtime**: 1495 ms
- **Memory**: 18.1 MB
- **Solution**: Sort first, then run-through looking at first numbers, skipping duplicates, then search for 2Sum with the remaining using left and right pointers.

### Problem 16
- **Name**: 3Sum Closest
- **Runtime**: 364 ms
- **Memory**: 14.1 MB
- **Solution**: Same as Problem 15, just simplified to only keep track of the best sum.

### Problem 17
- **Name**: Letter Combinations of a Phone Number
- **Runtime**: 34 ms
- **Memory**: 13.9 MB
- **Solution**: Directly generating all possible result by re-appending to result list. Dict for conversions.

### Problem 18
- **Name**: 4Sum 
- **Runtime**: 1607 ms
- **Memory**: 13.9 MB
- **Solution**: Same as Problem 5, but with an extra outer loop.

### Problem 19
- **Name**: Remove Nth Node From End of List 
- **Runtime**: 41 ms
- **Memory**: 13.8 MB
- **Solution**: Run through the singly-linked-list once, with one pointer lagging behind.

### Problem 20
- **Name**: Valid Parentheses
- **Runtime**: 54 ms
- **Memory**: 13.8 MB
- **Solution**: Keep a stack to stack the opening parens.

### Problem 22
- **Name**: Generate Parentheses
- **Runtime**: 51 ms
- **Memory**: 14.2 MB
- **Solution**: Recursively build the possible string, keeping track of the open parens left to make, and closing parens needed.

### Problem 23
- **Name**: Merge k Sorted Lists
- **Runtime**: 108 ms
- **Memory**: 17.7 MB
- **Solution**: Never keep empty lists. Implement a head to pull out the next nodes, pushing the next value of the linked-list. Override the ListNode's comparators for the heap.

### Problem 24
- **Name**: Swap Nodes in Pairs
- **Runtime**: 25 ms
- **Memory**: 13.9 MB
- **Solution**: Keep a lagging pointer, and just do some fancy swapping around with a temp variable.
 
### Problem 25
- **Name**: Reverse Nodes in k-Group
- **Runtime**: 65 ms
- **Memory**: 15.4 MB
- **Solution**: Created a sub-function to swap the first k elements of a singly-linked-list, applied it until the last group is shorter than k, apply it a second time to get the last group in order and return.
 
### Problem 26
- **Name**: Remove Duplicates from Sorted Array
- **Runtime**: 217 ms
- **Memory**: 15.5 MB
- **Solution**: Used a look-ahead pointer, and Python's del function to cut down the list.
 
### Problem 27
- **Name**: Remove Element
- **Runtime**: 45 ms
- **Memory**: 14 MB
- **Solution**: Pointer runs through the array, stoping to del any occurrences.
 
### Problem 28
- **Name**: Implement strStr()
- **Runtime**: 34 ms
- **Memory**: 13.8 MB
- **Solution**: Ran through the string, checking with Python's startswith function.
 
### Problem 29
- **Name**: Divide Two Integers
- **Runtime**: 57 ms
- **Memory**: 13.8 MB
- **Solution**: Since we can double numbers by adding them to themselves, we can essentially build up the result by computing the binary value, using the divisor to start instead of 1.
 
### Problem 30
- **Name**: Substring with Concatenation of All Words
- **Runtime**: 81 ms
- **Memory**: 14.2 MB
- **Solution**: Keep a dictionary count of remaining occurances of words needed in the string, scan through and update with words entering and leaving the scan area. Take care of modular offsets too.
 
### Problem 31
- **Name**: Next Permutation
- **Runtime**: 42 ms
- **Memory**: 13.8 MB
- **Solution**: Find the first value that is less than any of its previous, the search back for the next up to be swapped. Overall linear.
 
### Problem 32
- **Name**: Longest Valid Parentheses
- **Runtime**: 50 ms
- **Memory**: 14.8 MB
- **Solution**: Keep a stack of paren positions, and a boolean array of if they're popped or not, using the former to help fill the latter. Finally look for the longest streak in the boolean array.
 
### Problem 33
- **Name**: Search in Rotated Sorted Array
- **Runtime**: 56 ms
- **Memory**: 14.3 MB
- **Solution**: Do a binary search to find the rotation point (the true start of the array), then do another binary search for the target, correcting indicies with modular arithmetic.
 
### Problem 34
- **Name**: Find First and Last Position of Element in Sorted Array
- **Runtime**: 143 ms
- **Memory**: 15.6 MB
- **Solution**: Binary search twice for the start and end of the streaks, using different equality preferences to get the start and end respectively.
 
### Problem 35
- **Name**: Search Insert Position
- **Runtime**: 46 ms
- **Memory**: 14.9 MB
- **Solution**: Classic binary search, just watch out for off-by-one errors and edge cases.
 
### Problem 36
- **Name**: Valid Sudoku
- **Runtime**: 110 ms
- **Memory**: 13.9 MB
- **Solution**: Search the rows and columns using some indexing, keep track of values found with a set to check for duplicates.
 
### Problem 38
- **Name**: Count and Say
- **Runtime**: 71 ms
- **Memory**: 13.9 MB
- **Solution**: Recursively build up the solution.
 
### Problem 39
- **Name**: Combination Sum
- **Runtime**: 81 ms
- **Memory**: 14.5 MB
- **Solution**: Dynamic programming, memoizing smaller targets, and going down the list of candidates.
 
### Problem 40
- **Name**: Combination Sum II
- **Runtime**: 104 ms
- **Memory**: 14.3 MB
- **Solution**: Dynamic programming with an index similar to problem 39, but with a streak counter as well, and decided whether to keep a value, and how many.
 
### Problem 41
- **Name**: First Missing Positive
- **Runtime**: 1491 ms
- **Memory**: 59.6 MB
- **Solution**: Essentially a linear-time integer-based sort since we know the approximate range of values.
 
### Problem 42
- **Name**: Trapping Rain Water
- **Runtime**: 110 ms
- **Memory**: 15.8 MB
- **Solution**: Shave off the ends, then process from the left and right sides to the max in the array. Anything less than current maximum in the processing will be caught.
 
### Problem 43
- **Name**: Multiply Strings
- **Runtime**: 233 ms
- **Memory**: 13.8 MB
- **Solution**: This is just grade-school multiplication, with some ord/chr/ASCII arithmetic for string to int conversion.
 
### Problem 44
- **Name**: Wildcard Matching
- **Runtime**: 345 ms
- **Memory**: 25.7 MB
- **Solution**: Similar to problem 10, use dynamic programming: run through the pattern and string checking for matches at every step and memoizing sub-results. Also removing duplicate wild-cards makes things faster too.
 
### Problem 45
- **Name**: Jump Game II
- **Runtime**: 16446 ms
- **Memory**: 15.4 MB
- **Solution**: Kept track of the minimum costs at every step going forward. A more optimal solution would have been to keep track of the "maximum jump power" at each step.
 
### Problem 46
- **Name**: Permutations
- **Runtime**: 73 ms
- **Memory**: 14 MB
- **Solution**: Recurive approach to building up the permulations of the list.
 
### Problem 47
- **Name**: Permutations II
- **Runtime**: 70 ms
- **Memory**: 14.1 MB
- **Solution**: Same as Problem 46, except sorting first, and using a record of previous value placed in each loop to prevent re-counting a value at that level of recursion.
 
### Problem 48
- **Name**: Rotate Image
- **Runtime**: 53 ms
- **Memory**: 14 MB
- **Solution**: Iterate over the "layers" of the matrix, and on each layer run along it, doing a 4-way swap top-row to last-column to bottom-row to first-column.
 
### Problem 49
- **Name**: Group Anagrams
- **Runtime**: 119 ms
- **Memory**: 19.5 MB
- **Solution**: Sort the strings for anagram keys to a multi-set of all words found. Multi-set implemented as a dictionary of counts.
 
### Problem 50
- **Name**: Pow(x, n)
- **Runtime**: 34 ms
- **Memory**: 13.8 MB
- **Solution**: Python has pow build in as ** however implementing the recursive algorithm for integer powers is actually faster in performance.
 
### Problem 51
- **Name**: N-Queens
- **Runtime**: 108 ms
- **Memory**: 14.6 MB
- **Solution**: Generate permuations, recusively going down rows, keeping track of the restrictions from columns and diagonals updating the diagona restricitons on each row.
 
### Problem 52
- **Name**: N-Queens II
- **Runtime**: 63 ms
- **Memory**: 13.9 MB
- **Solution**: Same as problem 51, just counting solutions instead of having to construct the solution boards.
 
### Problem 53
- **Name**: Maximum Subarray
- **Runtime**: 803 ms
- **Memory**: 27.8 MB
- **Solution**: Keep track of the highest value reached. So long as our running total is positive we might as well keep it, otherwise ditch it looking for another streak staying in the positives.
 
### Problem 54
- **Name**: Spiral Matrix
- **Runtime**: 37 ms
- **Memory**: 13.8 MB
- **Solution**: Python's implementation of lists was useful: could shave off the sides of the matrix one at a time, going through the elements with the pop function and pop(0) for the front. Placing the element into the result after each operation.
 
### Problem 55
- **Name**: Jump Game
- **Runtime**: 624 ms
- **Memory**: 15.1 MB
- **Solution**: Keep a running total of the max jump length you can make running though the array. If it ever reaches 0 then we are stuck and report it as so.
 
### Problem 56
- **Name**: Merge Intervals
- **Runtime**: 252 ms
- **Memory**: 18.1 MB
- **Solution**: Sort the array of intervals first, then run through it keep track encompassing intervals, and appending to the result.
 
### Problem 57
- **Name**: Insert Interval
- **Runtime**: 150 ms
- **Memory**: 17.3 MB
- **Solution**: Binary searched for position of first insertion, then ran through all intervals needing to be merged from there.
 
### Problem 58
- **Name**: Length of Last Word
- **Runtime**: 39 ms
- **Memory**: 13.8 MB
- **Solution**: Strip trailing spaces first, then run through the string, keep track of the current streak. More optimal solution would be to run from the end.
 
### Problem 59
- **Name**: Spiral Matrix II
- **Runtime**: 46 ms
- **Memory**: 13.9 MB
- **Solution**: Break down the spiral rings into cases for the top-right-bottom-left and traverse through filling up the matrix.
 
### Problem 60
- **Name**: Permutation Sequence
- **Runtime**: 45 ms
- **Memory**: 13.9 MB
- **Solution**: We can enumerate permutations using the factorial number system, and construct a permutation from its number.
 
### Problem 61
- **Name**: Rotate List
- **Runtime**: 62 ms
- **Memory**: 13.9 MB
- **Solution**: First find the length of the list and the final node. Mod k so we don't rotate more than once, and also join the tail to the head to make it circular. With the length and k we know how many more steps to go before breaking the list so it's no longer circular and can return the head.
 
### Problem 62
- **Name**: Unique Paths
- **Runtime**: 58 ms
- **Memory**: 13.9 MB
- **Solution**: Closed-form solution via the stars-and-bars formula.
 
### Problem 63
- **Name**: Unique Paths II
- **Runtime**: 64 ms
- **Memory**: 14.2 MB
- **Solution**: Dynamic programming recursion with memoization.
 
### Problem 64
- **Name**: Minimum Path Sum
- **Runtime**: 111 ms
- **Memory**: 15.6 MB
- **Solution**: Dynamic programming by running through the grid and filling in costs of the shortest path.
 
### Problem 65
- **Name**: Valid Number
- **Runtime**: 34 ms
- **Memory**: 13.6 MB
- **Solution**: Wrote a regex to match the requirements.
 
### Problem 66
- **Name**: Plus One
- **Runtime**: 59 ms
- **Memory**: 13.8 MB
- **Solution**: Essentially the long addition algorithm, but with just the carry.
 
### Problem 67
- **Name**: Add Binary
- **Runtime**: 58 ms
- **Memory**: 13.8 MB
- **Solution**: Used Python's built-in functions for binary conversion.
 
### Problem 68
- **Name**: Text Justification
- **Runtime**: 35 ms
- **Memory**: 13.9 MB
- **Solution**: Run through the list of words keeping track of the minimum length of the line, and constructing the line when the limit is surpassed.
 
### Problem 69
- **Name**: Sqrt(x)
- **Runtime**: 61 ms
- **Memory**: 13.9 MB
- **Solution**: Newton's method for solving what number squared equals the input.
 
### Problem 70
- **Name**: Climbing Stairs
- **Runtime**: 45 ms
- **Memory**: 13.8 MB
- **Solution**: This is just the Fibonacci sequence. There is a closed-form solution via Binet's formula. Also a cached recursive approach works too.
 
### Problem 71
- **Name**: Simplify Path
- **Runtime**: 72 ms
- **Memory**: 13.8 MB
- **Solution**: I used regex pattern substitutions to solve this problem. A faster but more memory intensive approach would be to keep a stack of the path.
 
### Problem 72
- **Name**: Edit Distance
- **Runtime**: 89 ms
- **Memory**: 17.1 MB
- **Solution**: Dynamic programming with memoization. Run through the strings checking they match so far. Reaching an end means pure additions of deletions. mismatch means take the minimum of the 3 operations.
 
### Problem 73
- **Name**: Set Matrix Zeroes
- **Runtime**: 142 ms
- **Memory**: 14.8 MB
- **Solution**: Run through the matrix keeping a list of all indices where zeros are found. Then run through that list, setting the rows and columns accordingly.
 
### Problem 74
- **Name**: Search a 2D Matrix 
- **Runtime**: 102 ms
- **Memory**: 14.5 MB
- **Solution**: Used binary search across rows, then binary search across the found column. Technically binary search could be used across the entire matrix using modular arithmetic, but asymptotically the complexity is the same.
 
### Problem 75
- **Name**: Sort Colors
- **Runtime**: 48 ms
- **Memory**: 13.8 MB
- **Solution**: Count the number of appearances of each color, then fill in the matrix accordingly.
 
### Problem 76
- **Name**: Minimum Window Substring
- **Runtime**: 209 ms
- **Memory**: 14.7 MB
- **Solution**: Take a count of the required letters of t in a dict, then run through s with a lagged pointer, counting down the remaining letters of t needed from the dict. When a solution is reached incremented up the lagged pointer, until a tightest solution is found. Continue the run all the way through s to find the globally optimal solution in linear time.
 
### Problem 77
- **Name**: Combinations
- **Runtime**: 109 ms
- **Memory**: 18.8 MB
- **Solution**: Recursion with memoization, choosing whether or not to include the given element at each step.
 
### Problem 78
- **Name**: Subsets
- **Runtime**: 45 ms
- **Memory**: 13.9 MB
- **Solution**: Start with the set containing the empty set. Then run through the numbers and on each double the size the resulting set by appending a copy with the number added to each set.
 
### Problem 79
- **Name**: Word Search
- **Runtime**: 4254 ms
- **Memory**: 13.9 MB
- **Solution**: Run through possible starting locations, then start the search. Search is DFS, recursively going through posiitions and the string, keeping track of the positions searched to avoid re-use. 
 
### Problem 80
- **Name**: Remove Duplicates from Sorted Array II
- **Runtime**: 57 ms
- **Memory**: 14 MB
- **Solution**: Same as problem 26. Run through the array, checking two ahead for duplicates, and deleting while any are found.
 
### Problem 81
- **Name**: Search in Rotated Sorted Array II
- **Runtime**: 52 ms
- **Memory**: 14.6 MB
- **Solution**: Same as problem 33. But if the binary search is unsure if it's in a streak of duplicates revert to linear search.
 
### Problem 82
- **Name**: Remove Duplicates from Sorted List II
- **Runtime**: 56 ms
- **Memory**: 13.8 MB
- **Solution**: Run through the linked list, keeping track of the previous node. When duplicates are found continue deleting them until a non-duplicate is found, using the previous node. Also update the head if the deletion happens before there isn't a previous node to use.
 
### Problem 83
- **Name**: Remove Duplicates from Sorted List
- **Runtime**: 38 ms
- **Memory**: 13.8 MB
- **Solution**: Same as problem 82 but easier. Run through the list, and while the next node is a duplicate, remove it.
 
### Problem 84
- **Name**: Largest Rectangle in Histogram
- **Runtime**: 1497 ms
- **Memory**: 27.8 MB
- **Solution**: The main idea behind the optimal solution is a "monostack": keeping a stack with monotonically increasing elements. The idea here being that while we are adding to the stack there could be a better solution, but once we want to add an element that violates the property, then we should look back through out stack to see the possible solutions and remove them before adding the smaller constraining element.
 
### Problem 85
- **Name**: Maximal Rectangle
- **Runtime**: 447 ms
- **Memory**: 15.3 MB
- **Solution**: Same as problem 84. We can build our "height bars" by accumulating sum from the previous row on elements whose value is "1".
 
### Problem 86
- **Name**: Partition List
- **Runtime**: 64 ms
- **Memory**: 13.8 MB
- **Solution**: Run through the list, placing the lower nodes in their own side list, then concatenate the side list with the remaining list.
 
### Problem 87
- **Name**: Scramble String
- **Runtime**: 70 ms
- **Memory**: 14.4 MB
- **Solution**: Because letters must all stay with whatever side of a swap they are grouped on we can look at cuts which preserve this property on one side, then recursively check those sub-problems, memoizing the solutions by starting points and lengths of the sub-problems.
 
### Problem 88
- **Name**: Merge Sorted Array
- **Runtime**: 44 ms
- **Memory**: 13.9 MB
- **Solution**: Run through the arrays end-to-beginning, filling the merged array from the end back.
 
### Problem 89
- **Name**: Gray Code
- **Runtime**: 223 ms
- **Memory**: 22.6 MB
- **Solution**: Gray codes can be build recursively by taking the size lower problem and appending a mirrored copy, and prefixing 0 and 1 to the original and mirrored respectively.
 
### Problem 90
- **Name**: Subsets II
- **Runtime**: 62 ms
- **Memory**: 14.1 MB
- **Solution**: Similar to problem 78, but when a duplicate is found, count the number of duplicates and then multiply the number of subsets by the possible number of duplicates included.
 
### Problem 91
- **Name**: Decode Ways
- **Runtime**: 35 ms
- **Memory**: 14.2 MB
- **Solution**: Defined the problem recursively, running through the string, memoizing sub-results.
 
### Problem 92
- **Name**: Reverse Linked List II
- **Runtime**: 41 ms
- **Memory**: 13.9 MB
- **Solution**: Run through the list until the left node is found, then keep track of the new left and right nodes continuing forward placing the next nodes into the front of the new left. Watch out for edge cases.
 
### Problem 93
- **Name**: Restore IP Addresses
- **Runtime**: 54 ms
- **Memory**: 14.3 MB
- **Solution**: A recursive approach memoizing sub-results: look for all possible places to put a dot, checking the first number fits the criteria, then search the next depth with the remainign digits and 1 fewer dots to place.
 
### Problem 94
- **Name**: Binary Tree Inorder Traversal
- **Runtime**: 38 ms
- **Memory**: 13.9 MB
- **Solution**: DFS, appending the results of each sub-seach left-current-right.
 
### Problem 95
- **Name**: Unique Binary Search Trees II
- **Runtime**: 108 ms
- **Memory**: 15.7 MB
- **Solution**: Kept a list of values, and sent them down each side of the binary search tree recursively. This could probably be more efficient just using ranges.
 
### Problem 96
- **Name**: Unique Binary Search Trees
- **Runtime**: 57 ms
- **Memory**: 13.9 MB
- **Solution**: Recursive solution just considers number of possible elements to send down each branch, similar to problem 95. Closed form solution is possible via Catalan numbers.
 
### Problem 97
- **Name**: Interleaving String
- **Runtime**: 41 ms
- **Memory**: 14.2 MB
- **Solution**: Dynamic programming with memoization. This one is particularly elegant in it breakdown into a O(n^2) search over the two starting positions of the strings.
 
### Problem 98
- **Name**: Validate Binary Search Tree
- **Runtime**: 50 ms
- **Memory**: 16.4 MB
- **Solution**: Recursively run down the binary search tree, keeping track of the left and right bounds to ensure correctness.
 
### Problem 99
- **Name**: Recover Binary Search Tree
- **Runtime**: 130 ms
- **Memory**: 14.1 MB
- **Solution**: Morris traversal is the main method for traversing a tree without any kind of stack. It is an in-order traversal and so we can retain look for nodes that are out of order.
 
### Problem 100
- **Name**: Same Tree
- **Runtime**: 42 ms
- **Memory**: 13.9 MB
- **Solution**: We can perform a check for the current nodes matching, then check their left and rights together recursively.
 
### Problem 121
- **Name**: Best Time to Buy and Sell Stock
- **Runtime**: 985 ms
- **Memory**: 25.1 MB
- **Solution**: Run through the array, keep track of the lowest point found so far, and the highest point found since the low-point, along with the result being selling at the highest point before the next low-point is found.
 
### Problem 217
- **Name**: Contains Duplicate
- **Runtime**: 882 ms
- **Memory**: 26.1 MB
- **Solution**: Python's set will de-dupe the list for us and we can compare lengths in a one-liner.
 
### Problem 234
- **Name**: Palindrome Linked List
- **Runtime**: 932 ms
- **Memory**: 46.5 MB
- **Solution**: I just converted to list and compared reverse. O(1) space is possible by first counting the middle position, then reversing the second half, and walking through both comparing.

### Problem 238
- **Name**: Product of Array Except Self
- **Runtime**: 293 ms
- **Memory**: 22.5 MB
- **Solution**: Initial solution was to avoid the division by converting to logarithms, then subtracting and then re-exponentiating. Real answer is to run through the array forward accumulating, and then backwards accumulating.

### Problem 383
- **Name**: Ransom Note
- **Runtime**: 85 ms
- **Memory**: 14.2 MB
- **Solution**: Used the collections.Counter datastructure, which is essentially a multi-set, and comes with an 'inclusion' operator.

### Problem 412
- **Name**:i Fizz Buzz 
- **Runtime**: 69 ms
- **Memory**: 15 MB
- **Solution**: Simple if-block appending to a list.

### Problem 876
- **Name**: Middle of the Linked List
- **Runtime**: 47 ms
- **Memory**: 13.9 MB
- **Solution**: Ran through the list once to count, then again up to the middle.

### Problem 1337
- **Name**: The K Weakest Rows in a Matrix
- **Runtime**: 108 ms
- **Memory**: 14.3 MB
- **Solution**: Sum the rows and perform an argsort.

### Problem 1342
- **Name**: Number of Steps to Reduce a Number to Zero
- **Runtime**: 37 ms
- **Memory**: 13.8 MB
- **Solution**: Directly implemented the process.

### Problem 2251
- **Name**: Richest Customer Wealth
- **Runtime**: 62 ms
- **Memory**: 13.8 MB
- **Solution**: Sum rows and take the max.

