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
- **Name**: Implement strStr() (Find the Index of the First Occurrence in a String)
- **Runtime**: 34 ms
- **Memory**: 13.8 MB
- **Solution**: Ran through the string, checking with Python's `startswith` function. Better solution is to use Python's `index` function.
 
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
 
### Problem 37
- **Name**: Sudoku Solver
- **Runtime**: 928 ms
- **Memory**: 14 MB
- **Solution**: DFS works, modifying in-place and backtracking when an invalid leaf is found. A brief check for local feasibility of the solution is efficient.
 
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
- **Solution**: Run through the matrix keeping a list of all indices where zeros are found. Then run through that list, setting the rows and columns accordingly. To achieve a constant space solution, we can start by marking the first checking if the first row and first column will need to be set to all 0s, then use the first row and column to mark with 0s if they need to be all set.
 
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
 
### Problem 101
- **Name**: Symmetric Tree
- **Runtime**: 45 ms
- **Memory**: 13.9 MB
- **Solution**: Recursively look at pairs of nodes on opposite sides of the mirror.
 
### Problem 102
- **Name**: Binary Tree Level Order Traversal
- **Runtime**: 47 ms
- **Memory**: 14.3 MB
- **Solution**: BFS keeping track of the depth.
 
### Problem 103
- **Name**: Binary Tree Zigzag Level Order Traversal
- **Runtime**: 61 ms
- **Memory**: 14.1 MB
- **Solution**: Use a BFS-like search, creating a search queue split up by depths, where each level runs through the previous level's children in reverse.
 
### Problem 104
- **Name**: Maximum Depth of Binary Tree
- **Runtime**: 45 ms
- **Memory**: 16.3 MB
- **Solution**: DFS / DP by defining and empty node and value 0, then from the root and taking the max of left and right.
 
### Problem 105
- **Name**: Construct Binary Tree from Preorder and Inorder Traversal
- **Runtime**: 1930 ms
- **Memory**: 277.8 MB
- **Solution**: We can recursively determine which parts of our preorder and inorder traversals belong on the left and right sides. The root will be the first element of preorder, and everything to the left of the root in the inorder will belong on the left-side, and we can then take all the found elements off the front of the preorder to also go down the left side of the recursion, then put the remainder down the right side.
 
### Problem 106
- **Name**: Construct Binary Tree from Inorder and Postorder Traversal
- **Runtime**: 1242 ms
- **Memory**: 351.7 MB
- **Solution**: We can get our current root from the end of the post-order, then find the left and right sides of the tree from the inorder, which we can use to recurse down the left and right sides of the tree.
 
### Problem 107
- **Name**: Binary Tree Level Order Traversal II
- **Runtime**: 37 ms
- **Memory**: 14.2 MB
- **Solution**: Kept track of the nodes from each level, and on the next iteration run through those nodes in order to produce the next level. Return the final result in reverse order.
 
### Problem 108
- **Name**: Convert Sorted Array to Binary Search Tree
- **Runtime**: 113 ms
- **Memory**: 15.7 MB
- **Solution**: Recursively take the middle value, and slice the list into left and right sides, sending down the BST.
 
### Problem 109
- **Name**: Convert Sorted List to Binary Search Tree
- **Runtime**: 422 ms
- **Memory**: 20.4 MB
- **Solution**: Convert the linked-list to a list which can be sliced, and then recursively split the list in 2 to fill up the BST.
 
### Problem 110
- **Name**: Balanced Binary Tree
- **Runtime**: 86 ms
- **Memory**: 18.9 MB
- **Solution**: Recursively get heights of sub-trees, and check for validity of left and right sub-trees and if there are any violations found.
 
### Problem 111
- **Name**: Minimum Depth of Binary Tree
- **Runtime**: 1276 ms
- **Memory**: 55 MB
- **Solution**: Recursively check children for shortest path and return the min.
 
### Problem 112
- **Name**: Path Sum
- **Runtime**: 37 ms
- **Memory**: 15.1 MB
- **Solution**: Recursively send down the new target to left and right child nodes until a solution is found.
 
### Problem 113
- **Name**: Path Sum II
- **Runtime**: 62 ms
- **Memory**: 15.5 MB
- **Solution**: Recursively send down new target to left and right child nodes, and send back up list off all paths to be pre-pended to.
 
### Problem 114
- **Name**: Flatten Binary Tree to Linked List
- **Runtime**: 68 ms
- **Memory**: 15.2 MB
- **Solution**: Recursively flatten the left and right sides, returning the start and ends of each side to chain together.
 
### Problem 115
- **Name**: Distinct Subsequences
- **Runtime**: 1621 ms
- **Memory**: 154.9 MB
- **Solution**: DP over starting indices of the strings, memoizing sub-results.
 
### Problem 116
- **Name**: Populating Next Right Pointers in Each Node
- **Runtime**: 83 ms
- **Memory**: 15.5 MB
- **Solution**: One solution is to recursively pass down left and right adjacent pairs, which are then joined and recurse: thereby keeping the separate branches that should be adjacent together. Another solution is to use each level of nexts and a queue to run through and join the children.
 
### Problem 117
- **Name**: Populating Next Right Pointers in Each Node II
- **Runtime**: 49 ms
- **Memory**: 15.3 MB
- **Solution**: Keep track of the starting node of the next level, and use it as a queue to run through looking for children, keeping track of the last child found to append to.
 
### Problem 118
- **Name**: Pascal's Triangle
- **Runtime**: 62 ms
- **Memory**: 13.9 MB
- **Solution**: For each row, run though adjacent pairs of the previous row summing them.
 
### Problem 119
- **Name**: Pascal's Triangle II
- **Runtime**: 53 ms
- **Memory**: 13.9 MB
- **Solution**: We can use the fact that a given element of Pascal's triangle is given by the combination function.
 
### Problem 120
- **Name**: Triangle
- **Runtime**: 138 ms
- **Memory**: 14.9 MB
- **Solution**: DP running through each row and taking only the smaller total cost of the two possible parents. Essentially a simplified Dijkstra's.
 
### Problem 121
- **Name**: Best Time to Buy and Sell Stock
- **Runtime**: 985 ms
- **Memory**: 25.1 MB
- **Solution**: Run through the array, keep track of the lowest point found so far, and the highest point found since the low-point, along with the result being selling at the highest point before the next low-point is found.
 
### Problem 122
- **Name**: Best Time to Buy and Sell Stock II
- **Runtime**: 79 ms
- **Memory**: 15.3 MB
- **Solution**: Since we can only keep 1 until and can buy and sell on the same day, optimal strategy is to buy whenever the price will go up the next day and sell on the next day.
 
### Problem 123
- **Name**: Best Time to Buy and Sell Stock III
- **Runtime**: 1450 ms
- **Memory**:27.9 MB
- **Solution**: Linear time solution obtained by first running backwards through the prices keeping track of max future prices and therefore max possible future profit. Then run through forward, keeping track of minimum past prices, and therefore max profit up to given day, added with max future profit we can then linearly find the max possible profit overall.
 
### Problem 124
- **Name**: Binary Tree Maximum Path Sum
- **Runtime**: 109 ms
- **Memory**: 21.2 MB
- **Solution**: Keep track of the globally best solution. For every node consider the max values of both children, if them joined would give a best solution, and pass up the best child. Essentially a DFS with a global track.
 
### Problem 125
- **Name**: Valid Palindrome
- **Runtime**: 73 ms
- **Memory**: 20.1 MB
- **Solution**: Strip the string of non-alphanumeric characters, then compare with its reverse.
 
### Problem 126
- **Name**: Word Ladder II
- **Runtime**: 103 ms
- **Memory**: 14.2 MB
- **Solution**: BFS twice: the first time from beginWord to endWord to find the optimal distances to nodes along the path, then in reverse from endWord to beginWord to find the paths. This ensures that we only record the full paths for nodes that will on an optimal path. I included 2 ways to find neighboring nodes: by going over all letter-swap choices on each node (slower), or making a list of positions to swap letters from, each containing a map from the string with that letter removed to their corresponding words in wordList.
 
### Problem 127
- **Name**: Word Ladder
- **Runtime**: 532 ms
- **Memory**: 15 MB
- **Solution**: BFS will find optimal path. Go overy every letter-swapping for each word looking for other words in the next depth layer. Keep track of the depth so far and return it when solution is found.
 
### Problem 128
- **Name**: Longest Consecutive Sequence
- **Runtime**: 371 ms
- **Memory**: 38.7 MB
- **Solution**: Kept 2 dicts keeping track of the starts and ends of the consecutive sequences, updating as we run through the input.
 
### Problem 129
- **Name**: Sum Root to Leaf Numbers
- **Runtime**: 66 ms
- **Memory**: 14 MB
- **Solution**: DFS to find leaves and pass down the number so far, then return up with the sum.
 
### Problem 130
- **Name**: Surrounded Regions
- **Runtime**: 145 ms
- **Memory**: 15.2 MB
- **Solution**: The trick is to notice that regions with edges adjacent to the edge will transitively be blocked from being captured. All other regions will be captured. Therefore we can perform BFS from the edges to find all regions that are not captured, and fill in all the others.
 
### Problem 131
- **Name**: Palindrome Partitioning
- **Runtime**: 1156 ms
- **Memory**: 33.9 MB
- **Solution**: Ran through the string, greedily trying to expanding the indices encompassing each possible palidrome to make longer and longer ones where possible. With all the valid stard and end indices recursively build up all palindrome partitions using the indices to see possible places for the next partition.
 
### Problem 132
- **Name**: Palindrome Partitioning II
- **Runtime**: 3762 ms
- **Memory**: 520.6 MB
- **Solution**: DP, caching sub-results. For each index we look at all possible starting palindromes, then recurse to search afterwards. We can cache sub-results for indices, and also cache palindrome checks as well.
 
### Problem 133
- **Name**: Clone Graph
- **Runtime**: 71 ms
- **Memory**: 14.3 MB
- **Solution**: DFS, keeping a dictionary from node values to their copies.
 
### Problem 134
- **Name**: Gas Station
- **Runtime**: 694 ms
- **Memory**: 19 MB
- **Solution**: First check the loop has positive value by summing the gas minus the costs. Now since it's a non-decreasing loop imagine the graph showing the accumulated gas as a graph wrapped around a cylinder to show the cyclical nature: starting from anywhere if we do one full turn and identify the lowest point we can then rotate so it will always be at the bottom. Therefore identify the cumulative sum min index.
 
### Problem 135
- **Name**: Candy
- **Runtime**: 389 ms
- **Memory**: 16.8 MB
- **Solution**: 2-passes, making the minimum number of increases to satisfy the conditions. The first checks forwards increases, and will increase the current child's candy from the prev if need be, and similarly the second check goes backwards, ensuring the decreases are satisfied.
 
### Problem 137
- **Name**: Single Number II
- **Runtime**: 292 ms
- **Memory**: 16.3 MB
- **Solution**: Go through bit-by-bit counting up the appearances and then take the mod 3 to get the leftover bits and reveal the final number.
 
### Problem 138
- **Name**: Copy List with Random Pointer
- **Runtime**: 75 ms
- **Memory**: 15 MB
- **Solution**: A first run-through to gives each node a unique index identifier, then make a run-through to build up the copy-list and a dictionary mapping the unique indices to the new nodes, then a final run-through to set the random pointers in the new list using the mapping dict.
 
### Problem 139
- **Name**: Word Break
- **Runtime**: 45 ms
- **Memory**: 15 MB
- **Solution**: Make a trie of the dictionary words, then ran through the string looking for trie leaves, and when one is found, add the next possible starting point to a heap to continue the search. This is also solveable by just keeping an array the length of the string to represent valid possible starting points and then for each get all next possible starting points.
 
### Problem 140
- **Name**: Word Break II
- **Runtime**: 53 ms
- **Memory**: 13.9 MB
- **Solution**: Make a trie of the dictionary, then use DFS search, going to the next depth by word ends, with caching by position in the string to find all possible valid breaks, and construct the result as returned upwards.
 
### Problem 141
- **Name**: Linked List Cycle
- **Runtime**: 75 ms
- **Memory**: 17.6 MB
- **Solution**: Tortoise and hare algorithm for cycle detection in a linked list.
 
### Problem 142
- **Name**: Linked List Cycle II
- **Runtime**: 60 ms
- **Memory**: 17.5 MB
- **Solution**: Use the classic tortoise and hare algorithm to find the cycle, and then the starting point.
 
### Problem 143
- **Name**: Reorder List
- **Runtime**: 176 ms
- **Memory**: 23.9 MB
- **Solution**: First find the length of the list, then find the middle and split into two lists, then reverse the second list, then merge the two.

### Problem 144
- **Name**: Binary Tree Preorder Traversal
- **Runtime**: 33 ms
- **Memory**: 13.9 MB
- **Solution**: This is an easy recursive/DFS solution, appending the lists returned by sub-calls in the correct ordering prepended with the value of the current node.
 
### Problem 145
- **Name**: Binary Tree Postorder Traversal
- **Runtime**: 64 ms
- **Memory**: 13.9 MB
- **Solution**: This is an easy recursive/DFS solution, appending the lists returned by sub-calls in the correct ordering appended with the value of the current node. Essentially the same as problem 144.
 
### Problem 146
- **Name**: LRU Cache
- **Runtime**: 2120 ms
- **Memory**: 75.8 MB
- **Solution**: The LRU cache is a classic, the solution is to use a doubly-linked list to keep the order of last used, and a dictionay to the list nodes to allow random access.
 
### Problem 147
- **Name**: Insertion Sort List
- **Runtime**: 1505 ms
- **Memory**: 16.5 MB
- **Solution**: Keep track of the head of the sorted list, and the remaining unsorted list. Run through the unsorted list, and take each element and run up from the beginning of the sorted list, inserting it before the first element greater than itself is found (stable sort with strict inequality), using a prev and curr nodes to insert in the correct position.
 
### Problem 148
- **Name**: Sort List
- **Runtime**: 1121 ms
- **Memory**: 36.5 MB
- **Solution**: We can use mergesort to solve this problem. The lists lend themselves nicely to merging, however finding the midpoints requires 2 run-throughs at each step to find the middle node and split.
 
### Problem 149
- **Name**: Max Points on a Line
- **Runtime**: 328 ms
- **Memory**: 14.3 MB
- **Solution**: For each point, look at every other point, convert the lines intersecting into a standard format for same line: rise over run in lowest terms and positive x point closest to the y-intercept. These can be done quickly via gcd and mod operations. Handle edge cases for 0 rise or run. This allows us to create Counter dicts of the number of times a line is seen. Handle repeats in pairs of points. Fun!
 
### Problem 150
- **Name**: Evaluate Reverse Polish Notation
- **Runtime**: 97 ms
- **Memory**: 14.3 MB
- **Solution**: Implement the stack of numbers, and on each token check if it's an operator, if so pop the top 2 elements and apply the operator then append back to the stack, otherwise convert to an int and put back on the stack. Careful the division is implementated correctly. Convert the final result to an int.
 
### Problem 151
- **Name**: Reverse Words in a String
- **Runtime**: 66 ms
- **Memory**: 14.1 MB
- **Solution**: This is really easy in Python and can be done in one line. We can use Python's split to get the words, then string slicing to reverse the strings, and then join to recreate the output.
 
### Problem 152
- **Name**: Maximum Product Subarray
- **Runtime**: 135 ms
- **Memory**: 14.4 MB
- **Solution**: Passed through to find where the zeros were and compute streaks of non-zeroes between. Then ran through those streaks forward then backwards, keeping track of the maximum found, because if there are an odd number of negatives we want as many as possible, except either the first or last negative.
 
### Problem 153
- **Name**: Find Minimum in Rotated Sorted Array
- **Runtime**: 95 ms
- **Memory**: 14.1 MB
- **Solution**: Use binary search to find where the array has been rotated to by making sure the left and right pointers are on different sides of the starting point.
 
### Problem 154
- **Name**: Find Minimum in Rotated Sorted Array II
- **Runtime**: 126 ms
- **Memory**: 14.5 MB
- **Solution**: Binary search to find where the right and left are still on opposite sides of the rotation point. When caught in a duplicate, move up the pointers to break out.
 
### Problem 155
- **Name**: Min Stack
- **Runtime**: 168 ms
- **Memory**: 18.1 MB
- **Solution**: We can implement these O(1) operations back having both a regular Python list as a stack, and a second stack that only holds the min values from the stack. Could maybe be more memory efficient by only storing the indices to the current min?
 
### Problem 160
- **Name**: Intersection of Two Linked Lists
- **Runtime**: 161 ms
- **Memory**: 161 MB
- **Solution**: Solved by doing a single pass, keeping a set of all the seen nodes, waiting for an intersection to happen. A lower memory solution exists by counting the lengths of each list, and then lining the lists up to ensure the last nodes will be hit at the same time, and therefore the intersection will be hit at the same time on both and can therefore be checked.
 
### Problem 162
- **Name**: Find Peak Element
- **Runtime**: 51 ms
- **Memory**: 14 MB
- **Solution**: Use binary search: on each new midpoint check to see if it's increasing or decreasing, then pull up the left or right bound accordinly to tighten in on a peak.
 
### Problem 164
- **Name**: Maximum Gap
- **Runtime**: 3945 ms
- **Memory**: 30 MB
- **Solution**: Sorted order in linear time implies bucketsort. In this case we don't need a complete sort, but if we bucket the values along the complete range, then we can guaruntee the largest difference will cause the values to be pushed into separate buckets because the distance between the two must be larger than or equal the even-spacing distance.
 
### Problem 165
- **Name**: Compare Version Numbers
- **Runtime**: 36 ms
- **Memory**: 13.8 MB
- **Solution**: Split the string converting pieces to ints, then lengthen whichever is shorter with 0s, and then Python will do the compare.
 
### Problem 166
- **Name**: Fraction to Recurring Decimal
- **Runtime**: 32 ms
- **Memory**: 14 MB
- **Solution**: Representing fractional numbers in a radix. We can compute the digits past the decimal point by multiplying by 10 and taking the integers. A repeating decimal will show up when an already used remainder appears, whereas a remainder of 0 means there is no repeated decimal. Watch out for edge cases such as negatives.
 
### Problem 167
- **Name**: Two Sum II - Input Array Is Sorted
- **Runtime**: 186 ms
- **Memory**: 14.9 MB
- **Solution**: Run through the list, performing binary search on each element for its complement, for constant extra space.
 
### Problem 168
- **Name**: Excel Sheet Column Title
- **Runtime**: 40 ms
- **Memory**: 13.9 MB
- **Solution**: Almost like a base 26 number system, but need to offset by 1 at digit.
 
### Problem 169
- **Name**: Majority Element
- **Runtime**: 264 ms
- **Memory**: 15.6 MB
- **Solution**: Python's collections class makes this problem easy to solve in 1 line. However it is O(n) space, while an O(1) space solution exists via the Boyer-Moore voting algorithm:
 
### Problem 172
- **Name**: Factorial Trailing Zeroes
- **Runtime**: 35 ms
- **Memory**: 13.8 MB
- **Solution**: The number of trailing zeroes is the number of times 10 is a factor, which is the min of the number of 5 and 2 factors. These can be found without actually fully computing n! by going through all the lower numbers while would be multiplied. Even further using division we can count the numbers divisible by 5 and 2, but we also need to account for number divisible by 5 and 2 multiple times: just exponentiate the facts and divide to count the total number of factors. This is therefore a O(log(n)) time solution.
 
### Problem 173
- **Name**: Binary Search Tree Iterator
- **Runtime**: 80 ms
- **Memory**: 20.4 MB
- **Solution**: Similar to how a normal tree-traveral would go, keep a stack to keep track of current position in the tree. While the stack has values, there is a next: the top of the stack. When a value is popped, put its right child on the stack, and all left-descendants along with it.
 
### Problem 174
- **Name**: Dungeon Game
- **Runtime**: 71 ms
- **Memory**: 15.2 MB
- **Solution**: Dynamic programming, using the dungeon in-place. We can start from the end, and move backward through the possible rooms row by row, filling them in with the minimum difference in health between the current room and the final room. We can't store up future health for previous reductions, so we clamp to 0 instead of going negative. Increment by 1 to end with at least 1 health.
 
### Problem 179
- **Name**: Largest Number
- **Runtime**: 38 ms
- **Memory**: 13.9 MB
- **Solution**: Sort the numbers using a comparator which simpy checking which order they are best placed in.
 
### Problem 187
- **Name**: Repeated DNA Sequences
- **Runtime**: 115 ms
- **Memory**: 27.6 MB
- **Solution**: Run through all the length 10 slices of the string, incrementing their counts in a Counter. Filter the final results to have more than 1 occurance.
 
### Problem 188
- **Name**: Best Time to Buy and Sell Stock IV
- **Runtime**: 331 ms
- **Memory**: 78.9 MB
- **Solution**: Dynamic programming, recursive solution with memoization, using the day i, remaining transactions k, and if holding the stock boolean as the state.
 
### Problem 190
- **Name**: Reverse Bits
- **Runtime**: 54 ms
- **Memory**: 13.9 MB
- **Solution**: Bitshift the input down, while bitsifting the output up, setting the least significant digit of the output the least significant digit of the input.
 
### Problem 191
- **Name**: Number of 1 Bits
- **Runtime**: 65 ms
- **Memory**: 13.9 MB
- **Solution**: Original approach was to run through the binary representation by bitshifting down and extracting the least significant digit. However turns out there's a more optimal way: subtracting 1 will flip all bits up to and including the least significant 1, therefore taking the and operation will effectively remove the least significant 1.
 
### Problem 198
- **Name**: House Robber
- **Runtime**: 42 ms
- **Memory**: 14 MB
- **Solution**: DP by taking the max of the solution with taking the current house then skipping one, or skipping the current house. My original approach started at the beginning and looked forward, memoizing sub-results. However a better solution requires only constant extra memory: by solving forward and taking the max between previous results.
 
### Problem 199
- **Name**: Binary Tree Right Side View
- **Runtime**: 45 ms
- **Memory**: 14 MB
- **Solution**: DFS, prioritizing the right side, and keeping track of the depth. At each level append the first node seen to a global result list.
 
### Problem 200
- **Name**: Number of Islands
- **Runtime**: 303 ms
- **Memory**: 21.6 MB
- **Solution**: A "flood-fill" algorithm using BFS, and keeping track of the possible starting points remaining, and counting the number of terminations.
 
### Problem 201
- **Name**: Bitwise AND of Numbers Range
- **Runtime**: 108 ms
- **Memory**: 13.9 MB
- **Solution**: The only bits that will be preserved from ANDing all number in the range are the common leading 1s before there is a difference in bits. Run through the binary representations to fill up the result.
 
### Problem 202
- **Name**: Happy Number
- **Runtime**: 51 ms
- **Memory**: 16.2 MB
- **Solution**: We can solve this problem simply by using a set to check if we've seen the value before and proceeding with the process. However a more efficient solution is to use Floyd's cycle finding algorithm.
 
### Problem 206
- **Name**: Reverse Linked List
- **Runtime**: 51 ms
- **Memory**: 15.4 MB
- **Solution**: The head will become the new tail: keep taking nodes out of the linked list after the target new tail (original head), and placing them at the from the of list until the tail is actually the tail.
 
### Problem 207
- **Name**: Course Schedule
- **Runtime**: 117 ms
- **Memory**: 18.3 MB
- **Solution**: This is cycle detection in a directed graph. We loop over possible starting nodes, and run DFS on them, keeping track of which we still have to search, and which have been found in the current DFS run, and which have already been searched and determined to not contain any cycles.
 
### Problem 208
- **Name**: Implement Trie (Prefix Tree)
- **Runtime**: 229 ms
- **Memory**: 32.6 MB
- **Solution**: Implemented by encapsulating a dict to other Tries, then functions are defined recursively with string slicing. Uses a boolean to indicate an end.
 
### Problem 209
- **Name**: Minimum Size Subarray Sum
- **Runtime**: 914 ms
- **Memory**: 26.9 MB
- **Solution**: Two pointers, to grow and slide window.
 
### Problem 210
- **Name**: Course Schedule II
- **Runtime**: 266 ms
- **Memory**: 15.5 MB
- **Solution**: Construct the dependency graph and keep track of the number of inbound edges to each node. Nodes with no inbound edges represent classes that can be taken immediately. Remove their outbound edges from the graph, this represents this dependency being filled, and add any classes that now no longer have any inbounds. Repeat this process and check if all classes have been taken. This is Kahn's algorithm.
 
### Problem 211
- **Name**: Design Add and Search Words Data Structure
- **Runtime**: 14955 ms
- **Memory**: 77.7 MB
- **Solution**: Used a Trie, iterating over keys for wildcards.
 
### Problem 212
- **Name**: Word Search II
- **Runtime**: 1646 ms
- **Memory**: 14.4 MB
- **Solution**: First filtered all words to check their multi-set of letters was a subset of those on the board with Python's Counter. Next constructed a trie out of the words. Then iterate over starting points on the board, performing DFS keeping track of indices already searched. Go down the trie as we go down the DFS, checking our solution is still a candidate. When a solution is found, remove it from the trie, using the natural recursion of the DFS.
 
### Problem 213
- **Name**: House Robber II
- **Runtime**: 56 ms
- **Memory**: 13.9 MB
- **Solution**: Same as problem 198, just we can't have both the first and last house. So loop over the ability to keep one or the other.
 
### Problem 215
- **Name**: Kth Largest Element in an Array
- **Runtime**: 1291 ms
- **Memory**: 27.1 MB
- **Solution**: This is classic quickselect algorithm.
 
### Problem 216
- **Name**: Combination Sum III
- **Runtime**: 58 ms
- **Memory**: 14.1 MB
- **Solution**: We can use a simple DP over the triple of choices k remaining, n target remaining, and i number to consider adding. For cases where we add the number we can prepend to all sub-solution values. Memoization should help too.
 
### Problem 217
- **Name**: Contains Duplicate
- **Runtime**: 882 ms
- **Memory**: 26.1 MB
- **Solution**: Python's set will de-dupe the list for us and we can compare lengths in a one-liner.
 
### Problem 225
- **Name**: Implement Stack using Queues
- **Runtime**: 36 ms
- **Memory**: 16.3 MB
- **Solution**: The main issue is we'll need to be keeping the elements in the correct order for a stack, but in the queue. The only way to do this is to cycle the queue such that the pushed element can be put in the correct position.
 
### Problem 226
- **Name**: Invert Binary Tree
- **Runtime**: 65 ms
- **Memory**: 13.9 MB
- **Solution**: Recusively call the function on each node's children, and swap the results.
 
### Problem 228
- **Name**: Summary Ranges
- **Runtime**: 45 ms
- **Memory**: 16.4 MB
- **Solution**: Since the original list is sorted, we can simply add to each range one element at a time, and update the result once we find an element not fitting the range.
 
### Problem 229
- **Name**: Majority Element II
- **Runtime**: 107 ms
- **Memory**: 17.6 MB
- **Solution**: We can solve this in a 1-liner with Counter. However to use only constant space we should use the Boyer-Moore voting algorithm.
 
### Problem 230
- **Name**: Kth Smallest Element in a BST
- **Runtime**: 51 ms
- **Memory**: 18 MB
- **Solution**: DFS, returning the count of children so that a given node in the BST knows how many smaller elements there are, using a global boolean to indicate success and break out returning the solution.
 
### Problem 233
- **Name**: Number of Digit One
- **Runtime**: 25 ms
- **Memory**: 13.9 MB
- **Solution**: Each digit can either contribute a complete amount less than its value, or if it's a 1 contribute up to the remaining digits.
 
### Problem 234
- **Name**: Palindrome Linked List
- **Runtime**: 932 ms
- **Memory**: 46.5 MB
- **Solution**: I just converted to list and compared reverse. O(1) space is possible by first counting the middle position, then reversing the second half, and walking through both comparing.

### Problem 235
- **Name**: Lowest Common Ancestor of a Binary Search Tree
- **Runtime**: 121 ms
- **Memory**: 18.7 MB
- **Solution**: Generalized solution, not just for BSTs, is to do DFS, with each depth of recursion return either a set of the seached for elements or, after the LCA is found, returning the solution. However, since we have a BST, we can simply search for the node between the two searched for results.

### Problem 236
- **Name**: Lowest Common Ancestor of a Binary Tree
- **Runtime**: 128 ms
- **Memory**: 26.3 MB
- **Solution**: Recursively solve the problem by returning the current node as soon as it matches one of the two nodes. Otherwise if both the left and right children are returning nodes, then this is the LCA, otherwise just continue to send any found child node up, or none.

### Problem 238
- **Name**: Product of Array Except Self
- **Runtime**: 293 ms
- **Memory**: 22.5 MB
- **Solution**: Initial solution was to avoid the division by converting to logarithms, then subtracting and then re-exponentiating. Real answer is to run through the array forward accumulating, and then backwards accumulating.

### Problem 239
- **Name**: Sliding Window Maximum
- **Runtime**: 3123 ms
- **Memory**: 30.2 MB
- **Solution**: I originally solved this problems by using a max heap to keep track of the largest values in the window, and a dict as a multi-set to keep track of which values fell out of the window, cleaning up the heap's root using this mutli-set to ensure the max of the window was always correct (i.e. the heap would contain values inside the window, and previous, while the multi-set would keep track of values fallen out of the window that still needed to be removed from the heap, and would be removed once they reached the root). This gave a runtime of `O(n*log(n))`. A better solution is to use a monotonic queue: the front is always the largest value, and also keeps track of the index, and new values will pop from the end until they are monotonic property is satisfied, thereby removing elements that cannot ever by the largest in the window.

### Problem 240
- **Name**: Search a 2D Matrix II
- **Runtime**: 189 ms
- **Memory**: 20.3 MB
- **Solution**: Performing a binary search on each row is enough to satisfy the conditions. However a linear solution can also be obtained.

### Problem 242
- **Name**: Valid Anagram
- **Runtime**: 54 ms
- **Memory**: 14.4 MB
- **Solution**: Sorting the strings is one approach. A better one is to use Python's Counter class.

### Problem 258
- **Name**: Add Digits
- **Runtime**: 35 ms
- **Memory**: 13.8 MB
- **Solution**: We can do this efficiently with modular arithmetic and while loops.

### Problem 268
- **Name**: Missing Number
- **Runtime**: 149 ms
- **Memory**: 15.2 MB
- **Solution**: Use the triangular number formula to get what the sum should be, then subtract off the actual sum.

### Problem 287
- **Name**: Find the Duplicate Number
- **Runtime**: 641 ms
- **Memory**: 27.8 MB
- **Solution**: The solution that accommodates all the restrictions is the toritoise and hare algorithm treating the input array as a permutation (each element's value is the index of the next element mapped to). Finding the entrance to a cycle will guaruntee finding a duplicate. Also the first element 0 is guarunteed to be outside a cycle because no element can map to it.

### Problem 295
- **Name**: Find Median from Data Stream
- **Runtime**: 674 ms
- **Memory**: 35.9 MB
- **Solution**: 2 heaps: 1 for the values less or equal to the median, and 1 for the values equal to or greater than the median.

### Problem 297
- **Name**: Serialize and Deserialize Binary Tree
- **Runtime**: 154 ms
- **Memory**: 20.3 MB
- **Solution**: Many solutions exist of course. The one I went with first was a comma-separated list where every entry was a |-separated triple of (val, parent's index in the list, is left or right child). Worked slightly better than average. I bet there's a more optimal solution by constructing a numbering system of the different possible tree structures, using this to encode structure, then just a serialize the numbers as they appear in the tree. Using the problem's bounds this could probably be done with a serialization of 16-bit ints without need for separators. This should be optimal, perhaps with a compression algorithm on top.

### Problem 300
- **Name**: Longest Increasing Subsequence
- **Runtime**: 795 ms
- **Memory**: 14.1 MB
- **Solution**: Dynamic programming, keeping track of the minimum value reached to obtain a given streak length. This is therefore quadratic time complexity. However a more optimal approach is to notice that because of previous updates, only 1 streak value will need to be updated at most: therefore a binary search can be used.

### Problem 309
- **Name**: Best Time to Buy and Sell Stock with Cooldown
- **Runtime**: 66 ms
- **Memory**: 14.2 MB
- **Solution**: Since the state can be expressed as being at a given day either with or without the stock, from which the optimal solution going forward is independent of the path there, this implies a relatively linear DP. My first solution was a recursive one by state, where cooldown was expressed by jumping forward in time. I then read a more optimal solution, especially from a memory standpoint, was to keep track of 3 states: holding the stock, cooling down, not holding the stock. Then run forward keeping track of the max profit possible in each of the states.

### Problem 310
- **Name**: Minimum Height Trees
- **Runtime**: 1338 ms
- **Memory**: 25.8 MB
- **Solution**: Only 1 or two nodes in a tree can be the root of the minimum height tree. Used a BFS, similar to Kahn's algorithm to start from the leaves and work through each layer until either a single or two adjacent nodes are left.

### Problem 316
- **Name**: Remove Duplicate Letters
- **Runtime**: 43 ms
- **Memory**: 16.2 MB
- **Solution**: The solution is to use a variant of the monotonic stack. We have a stack that we will place the candidate letters into if the letter does not already appear. If the top of the stack is a larger letter and it will appear again we can pop it from the stack.

### Problem 319
- **Name**: Bulb Switcher
- **Runtime**: 40 ms
- **Memory**: 16.3 MB
- **Solution**: The number of times a bulb will be switched on an off will be equal to it's number of (improper) divisors. Divisors will come in pairs, unless the number is a square number. The count of the number of square numbers less than a given number is naturally its square root, rounded down.

### Problem 322
- **Name**: Coin Change
- **Runtime**: 2829 ms
- **Memory**: 14 MB
- **Solution**: Compute sums that can be made up to the target amount keeping track of the shortest path to each. To do this, from a given sum iterate over the coins that can add to the sum. This makes the solution time proportional to `coins.length * amount`. My initial attempt at DP over starting coin and target value didn't work because the time complexity then included looping over the number of copies of a given coin to include.

### Problem 327
- **Name**: Count of Range Sum
- **Runtime**: 6577 ms
- **Memory**: 52.6 MB
- **Solution**: Use the cumulative sum trick to be able to compute the range sum between any indices then use a balanced binary search tree which counts children to quickly find the counts of values within the range.

### Problem 328
- **Name**: Odd Even Linked List
- **Runtime**: 78 ms
- **Memory**: 16.7 MB
- **Solution**: Keep track of the head and tail of the even and odd new lists and build then up going through linearly, finally fastening the head of the even list to the tail of the off list.

### Problem 332
- **Name**: Reconstruct Itinerary
- **Runtime**: 93 ms
- **Memory**: 16.8 MB
- **Solution**: First sort the edges of the graph so we traverse them in lexicographic order in the first place, then use a depth-first search. Delete edges from the graph as they are traversed to increase efficiency, and restore them upon backtracking. Keep track of the count of edges used and return when all have been used.

### Problem 336
- **Name**: Palindrome Pairs
- **Runtime**: 5487 ms
- **Memory**: 377.8 MB
- **Solution**: Added each word to a trie for forwards and for backwards, keeping the indices tracked on leaves. Then for each word search it forward and backward in the opposite trie, and on each leaf check if the remainder is a palindrome. Also make sure not to double-count indices.

### Problem 338
- **Name**: Counting Bits
- **Runtime**: 80 ms
- **Memory**: 20.7 MB
- **Solution**: By removing the most significant binary digit we can a smaller number that has already been computed. As such we can run through the values onces and check previous solutions fill out the answer.

### Problem 341
- **Name**: Flatten Nested List Iterator
- **Runtime**: 68 ms
- **Memory**: 19.9 MB
- **Solution**: We can use a stack to keep track of the list at the current depth and also indices into it, so as to get a true iterator.

### Problem 342
- **Name**: Power of Four
- **Runtime**: 39 ms
- **Memory**: 16.2 MB
- **Solution**: Powers of 4 will have even numbered 0s in the bitstring with a leading 1. Check for this to get a quick solution.

### Problem 343
- **Name**: Integer Break
- **Runtime**: 40 ms
- **Memory**: 16.2 MB
- **Solution**: We will want as much symmetry between the numbers as possible, since we're multilying numbers with a fixed sum. Because of the small problem size we can run over all candidates, and the get their products, accounting for remainder.

### Problem 347
- **Name**: Top K Frequent Elements
- **Runtime**: 109 ms
- **Memory**: 19.7 MB
- **Solution**: Python actually comes with the functions to solve this out of the box: the `Counter` class to found frequencies, which comes with the `most_common(n)` function, which implements a heap under the hood: this gives a time complexity of O(`k*log(n)`), which has the worst case `k == n`. This question is close to sorting the input array: bucket sort is the obvious choice to beat the time requirements in O(`n`).

### Problem 371
- **Name**: Sum of Two Integers
- **Runtime**: 25 ms
- **Memory**: 13.8 MB
- **Solution**: Bit-manipulation to perform binary addition, treating the second input as the carries, and the first input as the solution accumulator. The hardest part is accounting for negatives via two's complement.

### Problem 373
- **Name**: Find K Pairs with Smallest Sums
- **Runtime**: 2494 ms
- **Memory**: 33.9 MB
- **Solution**: Use a heap to keep track of the minimums, the the indices to move up. Repeat popping and inserting the next sums up the lists until the result is filled.

### Problem 377
- **Name**: Combination Sum IV
- **Runtime**: 39 ms
- **Memory**: 14.1 MB
- **Solution**: DP, memoizing solutions to smaller targets.

### Problem 378
- **Name**: Kth Smallest Element in a Sorted Matrix
- **Runtime**: 285 ms
- **Memory**: 18.8 MB
- **Solution**: To get under the O(n^2) memory requirement, I man a heap of size n keeping track of the values of each row currently under consideration: take the lowest value out and move up the row and re-insert the new value. Repeating k times will lead to the lowest value overall in O(k * log(n)) time.

### Problem 380
- **Name**: Insert Delete GetRandom O(1)
- **Runtime**: 923 ms
- **Memory**: 61.3 MB
- **Solution**: For this problem I literally just implemented a simple hash table. In theory there should be completely random distribution over the buckets and within the buckets, so there shouldn't be an preference, though I suppose after a hash collision happens then there's a bias? The criteria for randomness is a little unclear, but the solution passes the test cases. A higher quality solution is to use a list of values and a dict mapping to the indices, that way inserting is appending, and removing is replacing with the last element.

### Problem 382
- **Name**: Linked List Random Node
- **Runtime**: 72 ms
- **Memory**: 17.5 MB
- **Solution**: A simple solution is to simply put the numbers into a regular array once, then sample from that. In the case the size of the linked-list is unknown, use resevoir sampling algorithm.

### Problem 383
- **Name**: Ransom Note
- **Runtime**: 85 ms
- **Memory**: 14.2 MB
- **Solution**: Used the collections.Counter datastructure, which is essentially a multi-set, and comes with an 'inclusion' operator.

### Problem 389
- **Name**: Find the Difference
- **Runtime**: 38 ms
- **Memory**: 16.3 MB
- **Solution**: We can use the Counter class to find the differences between the letters in the two strings and pick out the added letter.

### Problem 392
- **Name**: Is Subsequence
- **Runtime**: 45 ms
- **Memory**: 16.4 MB
- **Solution**: We should try to use up the letters from the substring as soon as possible running through the largers string.

### Problem 412
- **Name**: Fizz Buzz
- **Runtime**: 69 ms
- **Memory**: 15 MB
- **Solution**: Simple if-block appending to a list.

### Problem 416
- **Name**: Partition Equal Subset Sum
- **Runtime**: 446 ms
- **Memory**: 14.9 MB
- **Solution**: Since the partitions union to the complete set and their sums must be equal, then the sum of both must be equal to the sum of the entire set. If the set's sum is odd, then the answer is false. Now our target is half the set's sum. Picking elements of a set to match a target is the knapsack problem. Since the values are small enough we can cache reachable sums from previous elements in the array while going through, and from there add new reachable sums from the previously reachable. This in still exponential time in the worst case, but the bounds on this problem keep it reasonable.

### Problem 417
- **Name**: Pacific Atlantic Water Flow
- **Runtime**: 438 ms
- **Memory**: 15.6 MB
- **Solution**: Perform a "flood-fill" using BFS from the pairs of edges, and then take the intersection of the sets of nodes reached.

### Problem 421
- **Name**: Maximum XOR of Two Numbers in an Array
- **Runtime**: 849 ms
- **Memory**: 35.5 MB
- **Solution**: Build up the solution bit-by-bit by running over the bits and setting the next bit of the candidate solution, then checking if there are any prefixes in the nums which would xor to the prefix of the candidate solution.

### Problem 424
- **Name**: Longest Repeating Character Replacement
- **Runtime**: 1432 ms
- **Memory**: 14 MB
- **Solution**: For each unique character in the string run through with a fast and slow pointer, keeping track of remaining k and the streak length, pushing up the right pointer when possible, and dragging up the left pointer when needed.

### Problem 435
- **Name**: Non-overlapping Intervals
- **Runtime**: 1912 ms
- **Memory**: 52.9 MB
- **Solution**: Greedy algorithm: first sort the intervals, lowest start to highest start, then keep track of the end of the current interval, if it overlaps, then 1 interval has to go: increment the reuslt, and keep the interval that finishes first.

### Problem 437
- **Name**: Path Sum III
- **Runtime**: 464 ms
- **Memory**: 15.4 MB
- **Solution**: Go down recursively and at a leaf return an empty Counter. At a return, we can either continue all lowers sums by adding to their keys, or start a new sum path.

### Problem 438
- **Name**: Find All Anagrams in a String
- **Runtime**: 302 ms
- **Memory**: 15.1 MB
- **Solution**: Use a moving window updating a Counter of letters to check for anagrams.

### Problem 442
- **Name**: Find All Duplicates in an Array
- **Runtime**: 854 ms
- **Memory**: 21.7 MB
- **Solution**: Since all values are supposed to be positive use negating an int at a given index as a marker of already having seen it.

### Problem 443
- **Name**: String Compression
- **Runtime**: 57 ms
- **Memory**: 14 MB
- **Solution**: We can perform the operations in-place without an extra array using 2 pointers, one to read in the string, and the other to act as a cursor to write the compressed string as its able to be computed.

### Problem 445
- **Name**: Add Two Numbers II
- **Runtime**: 86 ms
- **Memory**: 16.5 MB
- **Solution**: Just use Python to do the work, turn the linked list into a Python integer do the addition, and turn it back.

### Problem 448
- **Name**: Find All Numbers Disappeared in an Array
- **Runtime**: 560 ms
- **Memory**: 26.1 MB
- **Solution**: We can simply turn the input into a set and perform set difference on the set of numbers 1 to n. A more optimal approach is to use the fact all the numbers are positive to borrow the negation bit to use as a marker on each index for if it was found or not.

### Problem 451
- **Name**: Sort Characters By Frequency
- **Runtime**: 81 ms
- **Memory**: 19.3 MB
- **Solution**: Python's Counter class makes this easy, we can use the frequency as the key for sorting.

### Problem 452
- **Name**: Minimum Number of Arrows to Burst Balloons
- **Runtime**: 1587 ms
- **Memory**: 59.8 MB
- **Solution**: Greedy algorithm: if we go through by end of interval we know at the first end a dart will also hit all intervals the started before hand. We can repeat this and we know it will be optimal to use as few darts as possible. My first solution I used a dict to a linked list to implement a queue of ends I could immediately access the middle via dict when I found starts ahead of th current best end, however I didn't need this as I could just skip over them in my loop.

### Problem 456
- **Name**: 132 Pattern
- **Runtime**: 368 ms
- **Memory**: 36.6 MB
- **Solution**: This is a monotonic stack problem: keep a stack of candidates for the largest value, and also our canidate for the second largest, which we can pop from the stack into. We place new candidates on the stack as they come up.

### Problem 458
- **Name**: Poor Pigs
- **Runtime**: 29 ms
- **Memory**: 16.1 MB
- **Solution**: Given the time to die and total time we get the number of rounds of testing we can do. Each pig could die in any round of testing, and so if we want to get the maximum number of total test outcomes this is `(tests+1)**pigs` possible outcomes, so we want to minimum pigs such that this number is equal to or greater than the number of buckets. Thus we can solve it with a simple logarithm.

### Problem 459
- **Name**: Repeated Substring Pattern
- **Runtime**: 859 ms
- **Memory**: 20 MB
- **Solution**: Used the fact we must have divisibility to filter out some possible substrings, then used the regex module to perform the check. A more efficient method is the check if the original string is contained in the concatenation with itself without the first and last letters.

### Problem 474
- **Name**: Concatenated Words
- **Runtime**: 374 ms
- **Memory**: 27.7 MB
- **Solution**: My first solution was to use a trie, to which I also added a method to search for concatenated words by branching the search back to the root every time a node that was a leaf (i.e. a possible word concatenated) was found. My second solution was more optimal, which was a straightforward DFS, building up subwords, and if in a previously found cache, then separately looking at the rest of the word to see if it concatenates.

### Problem 480
- **Name**: Sliding Window Median
- **Runtime**: 1149 ms
- **Memory**: 16.1 MB
- **Solution**: Used and upper heap and lower heap, with a Counter to keep track of values that need to be removed from the heaps. Similar to finding median of a stream.

### Problem 486
- **Name**: Predict the Winner
- **Runtime**: 30 ms
- **Memory**: 16.6 MB
- **Solution**: Use dynamic programming to memoize all sub-solutions of left and right indices.

### Problem 494
- **Name**: Target Sum
- **Runtime**: 366 ms
- **Memory**: 14.2 MB
- **Solution**: My initial solution was a simple recursive DP over the number we're looking at and the current target. However this solution is not optimal since it will memoize all the possible values of target for every step. A more optimal solution is to iterate over the numbers we either add of subtract to the target and create a new cache from the value at that given step, discarding the older cache as it's no longer needed.

### Problem 501
- **Name**: Find Mode in Binary Search Tree
- **Runtime**: 61 ms
- **Memory**: 20.1 MB
- **Solution**: In-order traversal of the BST will ensure we see all the duplicate values one after another so we can keep track of the count and update the mode canddiates as needed.

### Problem 502
- **Name**: IPO
- **Runtime**: 1042 ms
- **Memory**: 38.9 MB
- **Solution**: Out of all possible projects we can take at a given time, we should always take the one with highest profit. Therefore we need a priority queue, implemented as a heap, where we can insert projects we can take. We can also use a heap to hold all the projects sorted by capital required, and pop all we can undertake into the priority queue.

### Problem 515
- **Name**: Find Largest Value in Each Tree Row
- **Runtime**: 54 ms
- **Memory**: 19.2 MB
- **Solution**: We can use recursion keeping track of the depth to place and update maximum values in the result array.

### Problem 516
- **Name**: Longest Palindromic Subsequence
- **Runtime**: 1033 ms
- **Memory**: 250.9 MB
- **Solution**: Use dynamic programming to cache sub-problems over start and end indices of substrings deciding whether or not to keep letters.

### Problem 518
- **Name**: Coin Change II
- **Runtime**: 120 ms
- **Memory**: 42 MB
- **Solution**: Dynamic programming, recurse over position along the coins list, and amount remaining, memoizing sub-solutions.

### Problem 540
- **Name**: Single Element in a Sorted Array
- **Runtime**: 173 ms
- **Memory**: 23.8 MB
- **Solution**: We can use binary search by checking if elements with their matches are in even positions, compared to odd position by being offset by an unmatched prior element.

### Problem 542
- **Name**: 01 Matrix
- **Runtime**: 562 ms
- **Memory**: 21.7 MB
- **Solution**: Perform BFS, keeping track of which layer we are on.

### Problem 543
- **Name**: Diameter of Binary Tree
- **Runtime**: 66 ms
- **Memory**: 16.4 MB
- **Solution**: Recursively find max depths by recursing on children, then the max path is max sum of max depths between children for any node.

### Problem 557
- **Name**: Reverse Words in a String III
- **Runtime**: 44 ms
- **Memory**: 17.1 MB
- **Solution**: We can just split the words by spaces, and reverse each one before rejoining using list comprehension.

### Problem 567
- **Name**: Permutation in String
- **Runtime**: 133 ms
- **Memory**: 14 MB
- **Solution**: We can just keep counts of each letter appearing in the permutation, and having a sliding window through the array. We could optimize the check by keeping a count of letters that are out of balance so we don't need to complete equality check at each step.

### Problem 572
- **Name**: Subtree of Another Tree
- **Runtime**: 202 ms
- **Memory**: 15 MB
- **Solution**: Recursively search the tree, checking "is same tree" on each node. A more optimal approach would be to convert to a Merkle tree for instant checking.

### Problem 605
- **Name**: Can Place Flowers
- **Runtime**: 180 ms
- **Memory**: 14.5 MB
- **Solution**: Take a greedy approach, planting a flower whenever we can, and returning True as soon as we're able to hit the target, otherwise False.

### Problem 617
- **Name**: Merge Two Binary Trees
- **Runtime**: 87 ms
- **Memory**: 15.4 MB
- **Solution**: Recursive approach, using the fact that we can use original tree nodes instead of constructing new ones: as soon as we notice a lack of overlap we can just that node as is with its decendents.

### Problem 621
- **Name**: Task Scheduler
- **Runtime**: 667 ms
- **Memory**: 14.3 MB
- **Solution**: First get tasks and their frequencies, then greedily assign them with a priority queue by frequency. Decrement after each assignment, and put them into a cooldown queue, which is popped into the priority queue after cooldown is over.

### Problem 630
- **Name**: Course Schedule III
- **Runtime**: 1304 ms
- **Memory**: 20.2 MB
- **Solution**: The main limiting factor is the lastDay, so sort the courses by lastDay, then greedily add courses back-to-back. If the lastDay of an added course is less than the sum of the durations of all added courses so far, then we can correct this by removing the longest course added (possibly the most recent one), which is guarunteed to bring all currently added courses to valid positoons and now be under the lastDay cap. Continue until all courses have been gone through.

### Problem 632
- **Name**: Smallest Range Covering Elements from K Lists
- **Runtime**: 363 ms
- **Memory**: 21.4 MB
- **Solution**: Left and right pointers to make a sliding window. Keep one large sorted list keeping track of which original lists each came from. Start by "casting out" the right pointer until a valid pointer is found, then "real in" the left pointer, updating the solution while it remains valid.

### Problem 647
- **Name**: Palindromic Substrings
- **Runtime**: 2333 ms
- **Memory**: 176.8 MB
- **Solution**: DP using cache of all start and end indices for substrings to recursively check if they're valid palindromes, then count the True values in the cache.

### Problem 649
- **Name**: Dota2 Senate
- **Runtime**: 69 ms
- **Memory**: 16.4 MB
- **Solution**: The optimal strategy is to ban the next senator who would vote, since you are removing as much of your opponents chance to act as possible. We can simulate the process directly then, and use new string to represent the next round of remaining senators, and we can also use a count of the remaining senators in each party, and "lazy evaluation" of the bans queued up to make computation more efficient.

### Problem 654
- **Name**: Maximum Binary Tree
- **Runtime**: 206 ms
- **Memory**: 14.6 MB
- **Solution**: Recursively build up the tree by directly searching for the max index at each step, and only passing down the bounding indices for space efficiency.

### Problem 658
- **Name**: Find K Closest Elements
- **Runtime**: 322 ms
- **Memory**: 15.4 MB
- **Solution**: Use binary search to find the index of the closest element in the list (correcting for off-by-one errors), then linearly grow the indices to keep grabbing the next closest elements, and finally slice the array to return the final result.

### Problem 662
- **Name**: Maximum Width of Binary Tree
- **Runtime**: 100 ms
- **Memory**: 18.4 MB
- **Solution**: Recursively go down each level, and keep track of the furthest left and right positions found. The position of a node's child can be computed by doubling it's current position, since all other nodes have 2 children (including null nodes).

### Problem 673
- **Name**: Number of Longest Increasing Subsequence
- **Runtime**: 1192 ms
- **Memory**: 15.1 MB
- **Solution**: Pre-construct a balanced BST, with indicators about where values have officially been filled in, and which also saves the max-length path to each number and the number of such paths (updating as appropriate for duplicates). We can then slightly more quickly find all smaller-than nodes which have been reached and look for the longest path and how many there are. The final step is a complete search of the tree, in case of disparate longest paths.

### Problem 688
- **Name**: Knight Probability in Chessboard
- **Runtime**: 290 ms
- **Memory**: 16.5 MB
- **Solution**: This is a probability transition problem, which we can solve by iteratively spreading out the probability density. We can use a dict so we only store and work with reachable tiles.

### Problem 698
- **Name**: Partition to K Equal Sum Subsets
- **Runtime**: 161 ms
- **Memory**: 14 MB
- **Solution**: This is essentially a decision problem version of the bin packing problem. Being NP-Complete, we need to perform an exhaustive search, taking each element and tryig to place it in each of the bins, but we can speed things up be exiting early if no solution is found. We can also notice we'll want to place an element in a bin as soon as possible: we should never end up with the case where we choose to skip over placing an element in a bin which is still empty: the element should have either been already placed in a non-empty bin to keep building it, or placed in the empty to to start it: never just leave a bin empty.

### Problem 703
- **Name**: Kth Largest Element in a Stream
- **Runtime**: 117 ms
- **Memory**: 20.3 MB
- **Solution**: This is a obvious usecase for a heap. Push elements to the heap and pop until the size is k, the kth largest element will then be at the root. An improvement can be made by not trying to push elements which are less than than root.

### Problem 704
- **Name**: Binary Search
- **Runtime**: 290 ms
- **Memory**: 15.5 MB
- **Solution**: Classic binary search algorithm: use a left and right pointer, then check if the middle value is greather than or lesser than the target values and update the left and right pointers to the middle value accordingly to tighen the bounds until a solution is found.

### Problem 706
- **Name**: Design HashMap
- **Runtime**: 1446 ms
- **Memory**: 20.5 MB
- **Solution**: For a hash function I swapped the left and right sides of the number a XOR'd with a number with a well distributed hamming weight. After that used a load-balance of 0.75 to rehash, and used the typical dynamic array doubling in size implementation.

### Problem 705
- **Name**: Design HashSet
- **Runtime**: 748 ms
- **Memory**: 21.6 MB
- **Solution**: Main pieces needed is an array of buckets, which will double in size each time we surpass a given load, and a hash function. The hash function should be uniform, however for a quick solution I just used the mod of the integer keys.

### Problem 713
- **Name**: Subarray Product Less Than K
- **Runtime**: 1642 ms
- **Memory**: 16.6 MB
- **Solution**: This is a classic 2-pointer, which both monotonically increase, because the product can only increase. Increase the right pointer until a value less than k is found, set the left pointer there two, then increase the right pointer, accumulating to the product until it can't anymore, then increase the left pointer, dividing out of the accumulated product.

### Problem 714
- **Name**: Best Time to Buy and Sell Stock with Transaction Fee
- **Runtime**: 678 ms
- **Memory**: 23.4 MB
- **Solution**: There are 2 states: holding the stock and not holding the stock, and the way we get there doesn't matter, just that we have maximum profit. So we can step forward, updating with the fee applied upon selling, not keeping track of any other information.

### Problem 720
- **Name**: Longest Word in Dictionary
- **Runtime**: 142 ms
- **Memory**: 14.5 MB
- **Solution**: First sort the words by lexicographic order, then run through, keeping a set of the buildable words found so far. If a word's substring is in the buildable, then it too is, and we can also check if it is greater in length than the current best.

### Problem 725
- **Name**: Split Linked List in Parts
- **Runtime**: 49 ms
- **Memory**: 16.8 MB
- **Solution**: Run through the linked-list once to get its length, then we compute how many elements will go in each position in the result, and use the remainder to compute which will get extra elements.

### Problem 735
- **Name**: Asteroid Collision
- **Runtime**: 101 ms
- **Memory**: 17.6 MB
- **Solution**: We can use a stack to build this up in a single pass over the asteroids. Any moving to the right won't collide with those already processed, and for one moving to the left we can pop right-moving from the stack while they are smaller.

### Problem 744
- **Name**: Find Smallest Letter Greater Than Target
- **Runtime**: 125 ms
- **Memory**: 16.9 MB
- **Solution**: Binary search.

### Problem 745
- **Name**: Prefix and Suffix Search
- **Runtime**: 4900 ms
- **Memory**: 138 MB
- **Solution**: Use a trie to implement the fast searching, with the trick being because the words are guarunteed to be short, you can add all the possible suffixes with a delimiter after which comes the actual word, and this will cover all possible suffix-prefix cases. Implementing a Trie class with recusion was too slow, so barebone dicts with iteration was required.

### Problem 746
- **Name**: Min Cost Climbing Stairs
- **Runtime**: 50 ms
- **Memory**: 16.3 MB
- **Solution**: Because each step's optimal cost will be the min of the two previous steps we can just keep track of the two previous values and update proceeding through the array.

### Problem 767
- **Name**: Reorganize String
- **Runtime**: 33 ms
- **Memory**: 13.9 MB
- **Solution**: Use Python's Counter to get frequencies. Use the most frequent element to make buckets of adjacent characters, which we can then run over placing each new character in the next bucket. We're guarunteed to have at least 1 character between each of the same type.

### Problem 779
- **Name**: K-th Symbol in Grammar
- **Runtime**: 26 ms
- **Memory**: 16.2 MB
- **Solution**: We notice the pattern actually keeps its symbols fixed since the replacements for the symbols start with the symbols themselves, and that doubling ones position in the pattern doesn't change the symbol, but stepping forward by 1 does, therefore the position of each 1 is where the hamming weight of the index is odd. This makes for a short answer by counting the 1s in the bits of the index.

### Problem 783
- **Name**: Minimum Distance Between BST Nodes
- **Runtime**: 43 ms
- **Memory**: 13.9 MB
- **Solution**: Recursive tree traversal to put the values into a list, which can then be sorted and take the differences between adjacent elements to find the min.

### Problem 784
- **Name**: Letter Case Permutation
- **Runtime**: 62 ms
- **Memory**: 14.6 MB
- **Solution**: Run through all letters of the string, checking if lowercase and uppercase are different, if so double the result size and append the lowercase to the first half and uppercase the second half, otherwise just append to all.

### Problem 785
- **Name**: Is Graph Bipartite?
- **Runtime**: 178 ms
- **Memory**: 16.7 MB
- **Solution**: We can use a search algorithm, BFS or DFS, to color a neighbors of each node the opposite of the current node, and return false if there's a violation.

### Problem 787
- **Name**: Cheapest Flights Within K Stops
- **Runtime**: 483 ms
- **Memory**: 15.7 MB
- **Solution**: Essentially a modified BFS, where keys ared based on distance traverse from the the src node. Optimal cost is still tracked. There is probably a Dijkstra solution that's faster.

### Problem 797
- **Name**: All Paths From Source to Target
- **Runtime**: 110 ms
- **Memory**: 17.5 MB
- **Solution**: Because we are working with a DAG a simple recursive DFS will work fine, and we can use Python's functools.cache to avoid repeating computations.

### Problem 808
- **Name**: Soup Servings
- **Runtime**: 62 ms
- **Memory**: 16.4 MB
- **Solution**: The trick with this problem is that because of the exponential nature of the problem solutions converge to probability 1 after a large number of iterations. We can write out the dynamic programming version, and run it forward, only keeping track of 4 A states at a time and all corresponding B states probability (unless invalid). We can find a value of 1000 is sufficient for the required accuracy.

### Problem 815
- **Name**: Bus Routes
- **Runtime**: 510 ms
- **Memory**: 54.5 MB
- **Solution**: We can think of the problem as a bipartite graph between bus stops and bus routes, then run BFS to find the route using the fewest bus routes.

### Problem 823
- **Name**: Binary Trees With Factors
- **Runtime**: 396 ms
- **Memory**: 16.3 MB
- **Solution**: Dynamic programming with memoization, we find all the ways to build each possible number, and then if its a factor of another number all its possible subtrees are possible subtrees.

### Problem 828
- **Name**: Count Unique Characters of All Substrings of a Given String
- **Runtime**: 3426 ms
- **Memory**: 14.7 MB
- **Solution**: Solve this problem by counting the number of substrings in which a given letter appears once: summing over all letters is the same as summing the lengths of all substrings with unique letters. For each letter run through the string keeping track of the last position the character was seen, and the distance to the previous sighting of the character before that. We can update the result whenever a new sighting is found by counting the pairs of choices between indices before and including the previous sighting with the indices after the previous sighting (including none), which can be computed by a simple multiplication. This allows for a single pass for each letter.

### Problem 837
- **Name**: New 21 Game
- **Runtime**: 96 ms
- **Memory**: 16.8 MB
- **Solution**: We can solve this problem efficiently by maintaining a sliding window of the sum of probabilities of the last k elements. A new element is equally likely across 1/maxPts to receive the probability of any in the window. As soon as we pass k we drop elements from the probability.

### Problem 844
- **Name**: Backspace String Compare
- **Runtime**: 30 ms
- **Memory**: 14 MB
- **Solution**: Build up resulting strings literally: pop the end whenever a backspace character is encountered, then compare the 2.

### Problem 852
- **Name**: Peak Index in a Mountain Array
- **Runtime**: 610 ms
- **Memory**: 30.1 MB
- **Solution**: We can use binary search to find the peak and check neighbors to see if they're on the left or right side.

### Problem 859
- **Name**: Buddy Strings
- **Runtime**: 59 ms
- **Memory**: 16.6 MB
- **Solution**: Run through the strings together, checking for mismatched. Can only have 2 at most, and if there are none need to check there are double letters to swap, so keep letter count. Careful the edge cases on this one.

### Problem 863
- **Name**: All Nodes Distance K in Binary Tree
- **Runtime**: 71 ms
- **Memory**: 14.4 MB
- **Solution**: Two parts: search down to find the target node, then return back up with distance remaining. Recurse down again at each node to grab the relevant nodes.

### Problem 864
- **Name**: Shortest Path to Get All Keys
- **Runtime**: 484 ms
- **Memory**: 25.7 MB
- **Solution**: We can get the shortest path using BFS. We can keep track of the full state in the search graph by the position and which keys are collected.

### Problem 872
- **Name**: Leaf-Similar Trees
- **Runtime**: 67 ms
- **Memory**: 13.9 MB
- **Solution**: Recursively look for leaves, and append the lists in order, then compare for the two trees.

### Problem 875
- **Name**: Koko Eating Bananas
- **Runtime**: 356 ms
- **Memory**: 15.5 MB
- **Solution**: We can put bounds on the answer, because k must be at most the number of bananas in the largest pile, and greater than 0. We can then binary search for the solution on the cusp when when if becomes infeasible.

### Problem 876
- **Name**: Middle of the Linked List
- **Runtime**: 47 ms
- **Memory**: 13.9 MB
- **Solution**: Ran through the list once to count, then again up to the middle.

### Problem 880
- **Name**: Decoded String at Index
- **Runtime**: 41 ms
- **Memory**: 16.1 MB
- **Solution**: Keep track of the what the resultant length of the operations would be up will we surpass k, then start undoing the operations, using modular arithmetic to see where k would be pointing to in a string before multuplying it. Use a stack to keep track of the operations and final characters.

### Problem 894
- **Name**: All Possible Full Binary Trees
- **Runtime**: 255 ms
- **Memory**: 30.9 MB
- **Solution**: We can send down target sizes to each child of a nodes, and then we get a recursive subproblem.

### Problem 895
- **Name**: Maximum Frequency Stack
- **Runtime**: 540 ms
- **Memory**: 23 MB
- **Solution**: The max frequency can only change by at most 1 on a given operation, so keep track of its value, then have a map of values to their frequencies, then frequencies to stack. That way when popped the max frequency can be found and most recent returned, and for a value it's frequency and be found quickly and incremented and added to the next frequency stack.

### Problem 896
- **Name**: Monotonic Array
- **Runtime**: 802 ms
- **Memory**: 30.3 MB
- **Solution**: We can use 2 booleans to keep track of if the array is a candidate for monotone increasing or decreasing, plus another viarable for the previous value seen. If ever the array isn't viable for either we can immediately return the result of False, otherwise it is True.

### Problem 904
- **Name**: Fruit Into Baskets
- **Runtime**: 1280 ms
- **Memory**: 20.1 MB
- **Solution**: Since only 2 types are allowed, we only need to look for continuguous streaks of 2 types. We can run through the array once, and keep track of the 2 types currently under consideration and the last time each type was seen. Upon a new type we discard the other that isn't adjacent, and reupdate the length of our current streak.

### Problem 905
- **Name**: Sort Array By Parity
- **Runtime**: 79 ms
- **Memory**: 17 MB
- **Solution**: Just return the arrays joined, filtered by even and odds respectively.

### Problem 909
- **Name**: Snakes and Ladders
- **Runtime**: 128 ms
- **Memory**: 14 MB
- **Solution**: BFS will find the shorest path, so BFS to the solution and return when it is found, keeping track of the min distances to each location.

### Problem 912
- **Name**: Sort an Array
- **Runtime**: 2054 ms
- **Memory**: 32.7 MB
- **Solution**: For nlogn performance, we should use either mergesort,heapsort or quicksort (technically bucketsort and radix sort as well, but they work much better on lower cardinality problem). To minimize the space needed we should perform the sort in-place. Mergesort it the easiest to implement, however doing in place is tricky, so I used a buffer.

### Problem 918
- **Name**: Maximum Sum Circular Subarray
- **Runtime**: 551 ms
- **Memory**: 19 MB
- **Solution**: Kadane's algorithm, but for the ciruclar array notice that if the solution is one which falls off the bounds, then it is the complement with the minimum subarray: we can therefore compute the completment, and get that solution to check as well. Watch out for edge cases that would accidentally include empty subarrays.

### Problem 920
- **Name**: Number of Music Playlists
- **Runtime**: 119 ms
- **Memory**: 16.4 MB
- **Solution**: Start with the total number of playlists wihout "at least once" constraint: we can use the usual combinatoric approach of number of choices at each step. Then to remove the cases of not using a song we subtract off the subproblems with fewer songs, using the choose function to account for all combinations.

### Problem 926
- **Name**: Flip String to Monotone Increasing
- **Runtime**: 509 ms
- **Memory**: 16 MB
- **Solution**: Wherever we choose to "split" the string into a 0s half and 1s half, we can count the number of flips needed on each side. We can compute this instantly by counting up the accumulated count so far, and the total number of 0s since we can take the difference with the current count of 0s to get the number of flips to 1s remaining. We run over the entire string like so and take the min. Initialize values use that it counts the case where the entire string gets changed to 1s.

### Problem 935
- **Name**: Knight Dialer
- **Runtime**: 630 ms
- **Memory**: 16.2 MB
- **Solution**: We can keep track of the transitions and apply them over and over accumulating the results. A more efficient method is to construct the transition matrix and use fast exponentiation on it.

### Problem 938
- **Name**: Range Sum of BST
- **Runtime**: 579 ms
- **Memory**: 23 MB
- **Solution**: Recursive search, using the BST structure, to navigate where further searching can be done.

### Problem 947
- **Name**: Validate Stack Sequences
- **Runtime**: 71 ms
- **Memory**: 14.2 MB
- **Solution**: Since all the values are distinct, we just have to ensure all the pops can happen by iterating through them. If a pop can't currently happen, push to the stack until it can. If we run out of pushes before we finish then return False since it's invalid. If successful return True.

### Problem 953
- **Name**: Verifying an Alien Dictionary
- **Runtime**: 38 ms
- **Memory**: 13.9 MB
- **Solution**: Create a map from the characters to their positions, then we can convert the strings into lists of ints, and check if sorting makes a difference.

### Problem 958
- **Name**: Check Completeness of a Binary Tree
- **Runtime**: 40 ms
- **Memory**: 13.9 MB
- **Solution**: We can use BFS using the fact that level sets must match powers of 2 except for the final layer. Now for the final layer we must also check that every node is as far left as possible: we can do this by keeping track of when we meet a missing node, and making sure we don't find any other nodes afterwards.

### Problem 973
- **Name**: K Closest Points to Origin
- **Runtime**: 1730 ms
- **Memory**: 18.3 MB
- **Solution**: One easy method is to compute all the distances and perform and argsort on the result. Interesting to note KD trees are also a useful datastructure of such problems. Quickselect would probably be the fastest, though a heap is also quite fast.

### Problem 974
- **Name**: Subarray Sums Divisible by K
- **Runtime**: 342 ms
- **Memory**: 18.9 MB
- **Solution**: Keep a running count of the number times we've seen a given accumulated sum mod K. Because if we see the same sum mod K, then any previous times we say the same value we could chop the array there to get a subarray sum of 0, i.e. divisible by K.

### Problem 980
- **Name**: Unique Paths III
- **Runtime**: 95 ms
- **Memory**: 20.3 MB
- **Solution**: This is counting the number of Hamiltonian paths with a given start and end. Just checking for existence is NP-Complete, so we essentially have to brute-force with DFS, but we can add some optimizations, such as memoization. Another idea for an optimization would be to use Ore's theorem for pruning: it applies only Hamiltonian cycles rather than paths, but if we imagine adding an extra node connected only to the given start and end nodes then we can transform this problem into a Hamiltonian cycle problem and apply the theorem.

### Problem 983
- **Name**: Minimum Cost For Tickets
- **Runtime**: 91 ms
- **Memory**: 13.9 MB
- **Solution**: Dynamic Programming: keep a running min-cost, and update forward from each day on the minimum cost to get there.

### Problem 986
- **Name**: Interval List Intersections
- **Runtime**: 204 ms
- **Memory**: 14.9 MB
- **Solution**: Two pointers running through the two lists, checking for interval overlaps, and then adding the overlappign interval to the result (overlapping interval will be the max of both starts, and the mins of boths ends: i.e. the intersection). If there's no overlap the earliest starting one is incremented to catch up, if there is overlap the soonest ending one is incremented to check for more overlaps.

### Problem 989
- **Name**: Add to Array-Form of Integer
- **Runtime**: 313 ms
- **Memory**: 15 MB
- **Solution**: We can just use Python's conversion functions to do the work for us.

### Problem 995
- **Name**: Minimum Number of K Consecutive Bit Flips
- **Runtime**: 1485 ms
- **Memory**: 18.9 MB
- **Solution**: Greedy solution can be used to push the first appearance of a 0 back until all the 0s lie in the final K values. If there are 0s remaining then the problem is indeed unsolveable. So be able to do this in one pass quickly, we can use a queue to keep track of when we last needed a flip, and so if the current value should flip its value or not.

### Problem 997
- **Name**: Squares of a Sorted Array
- **Runtime**: 348 ms
- **Memory**: 16.2 MB
- **Solution**: The easy solution is a 1-liner in Python. However the linear time solution uses the fact the original array is sorted: simply need to merge the original negatives with the positives into the resultant array.

### Problem 1020
- **Name**: Number of Enclaves
- **Runtime**: 942 ms
- **Memory**: 22.4 MB
- **Solution**: Simple DFS/BFS search/flood-fill, to check which connected islands touch the border or not.

### Problem 1035
- **Name**: Uncrossed Lines
- **Runtime**: 232 ms
- **Memory**: 24.5 MB
- **Solution**: We can solve this problem with dynamic programming by noticing we can use sub-solutions: in any subsolution we should start with the leftmost elements from each list and then look at the moves we can makes from there, which each spawn new states with the leftmost elements in positions that can never be further left.

### Problem 1061
- **Name**: Lexicographically Smallest Equivalent String
- **Runtime**: 48 ms
- **Memory**: 13.8 MB
- **Solution**: Essentially the same as finding connected components on an undirected graph. The Union-Find datastructure is perfect for this, and can be implemented with a single fixed-size array. We can handle the characters by using Python's ord and char, offsetting by ord('a'), and make sure each set maps to the lexicograhically smallest by making the union operation favor the parent of lowest value. This is the first time I got 100% on memory usage.

### Problem 1071
- **Name**: Greatest Common Divisor of Strings
- **Runtime**: 30 ms
- **Memory**: 13.9 MB
- **Solution**: Increasingly append to common divisor candidate while the prefixes are the same, and record whenever a valid candidate is found.

### Problem 1095
- **Name**: Find in Mountain Array
- **Runtime**: 48 ms
- **Memory**: 17 MB
- **Solution**: Binary search to find the peak, checking if rising or falling to determine which side. Then binary search the left followed by right, also check the start index, peak, and final index, in order to find the minimum index occurence.

### Problem 1125
- **Name**: Smallest Sufficient Team
- **Runtime**: 522 ms
- **Memory**: 25.3 MB
- **Solution**: Since this in an NP-hard problem we need to do DP over the smallest dimension available, in this case skills. We can converts the skills set to a bitset representation, then search over that. It doesn't matter how to got to a given skills covering, just we need to find the smallest set to cover the rest, so check each person if they contribute new skills and if so search the new skillsets, keeping the smallest complete covering.

### Problem 1129
- **Name**: Shortest Path with Alternating Colors
- **Runtime**: 99 ms
- **Memory**: 14.4 MB
- **Solution**: BFS, just adding the last color visited as an extra parameter to the search space. More efficient would be to alternate between searching red and blue, and use the alternating colors with "layers" instead of a search queue.

### Problem 1137
- **Name**: N-th Tribonacci Number
- **Runtime**: 38 ms
- **Memory**: 13.8 MB
- **Solution**: Use the classic iterative approach with values to keep track of. Like Fibonacci numbers, this is a linear recurrence relation with constant coefficients, and so a closed-form solution is possible via matrix diagonalization.

### Problem 1140
- **Name**: Stone Game II
- **Runtime**: 861 ms
- **Memory**: 20.5 MB
- **Solution**: Classic dynamic programming for optimal game tree search. Since every turn forces the number of rock piles to be lower we can memoize over (piles remaining/position, M, turn).

### Problem 1160
- **Name**: Find Words That Can Be Formed by Characters
- **Runtime**: 171 ms
- **Memory**: 16.9 MB
- **Solution**: We can use Python's Counter class and it's comparator to quickly solve this problem.

### Problem 1161
- **Name**: Maximum Level Sum of a Binary Tree
- **Runtime**: 324 ms
- **Memory**: 21 MB
- **Solution**: Use a tree traversal while keeping track of the current level, and all the levels sums.

### Problem 1162
- **Name**: As Far from Land as Possible
- **Runtime**: 417 ms
- **Memory**: 43.9 MB
- **Solution**: Solved using Scipy's distance_transform_cdt, which is much more efficient than normal BFS. Must also turn the grid into a Numpy array. This is the 3rd time I've gotten 100%, then time on timing, while the memory was terrible.

### Problem 1203
- **Name**: Sort Items by Groups Respecting Dependencies
- **Runtime**: 578 ms
- **Memory**: 32.7 MB
- **Solution**: Dependency respecting implies topological sorting, the extra criteria of needing to be in adjacent groups means the groups will need to be in topological ordering as well: first construct the graphs of groups, topologically sort them with Kahn's algorithm, then within each group topologically sort the items. Kahn's algorithm will report a failed sort at any step.

### Problem 1207
- **Name**: Unique Number of Occurrences
- **Runtime**: 80 ms
- **Memory**: 14.1 MB
- **Solution**: Used Python's Counter class along sets to get unique count values and compare the lengths.

### Problem 1218
- **Name**: Longest Arithmetic Subsequence of Given Difference
- **Runtime**: 579 ms
- **Memory**: 30.11 MB
- **Solution**: Run through the array and for each value seen add it plus the difference into a dict holding the length of the streak so far. When a value is in the dict we can carry forward the streak.

### Problem 1220
- **Name**: Count Vowels Permutation
- **Runtime**: 563 ms
- **Memory**: 56.7 MB
- **Solution**: We can solve this fairly easily with recursive dynamic programming an memoization keeping track of the previous vowel, however we could reduce memory by doing bottom-up dynamic programming.

### Problem 1254
- **Name**: Number of Closed Islands
- **Runtime**: 126 ms
- **Memory**: 15.5 MB
- **Solution**: Use a DFS/BFS to reach over each each cell in the grid and keep track of connected landmasses and if they reach the border or not.

### Problem 1269
- **Name**: Number of Ways to Stay in the Same Place After Some Steps
- **Runtime**: 270 ms
- **Memory**: 59.2 MB
- **Solution**: The problem is the same in reverse. So we can do dynamic programming over positon and number of steps to take left. We can also prune all states where returning to the origin would be impossible because of distance.

### Problem 1319
- **Name**: Number of Operations to Make Network Connected
- **Runtime**: 508 ms
- **Memory**: 44 MB
- **Solution**: Used a bfs while there are unsearched nodes to find all the connected components. Also if there is an edge to a previously searched node, then it is an excess edge and can be used to connect components in an operation. Check if there are sufficient excess edges for connected components, and if so return 1 less than the number of components.

### Problem 1337
- **Name**: The K Weakest Rows in a Matrix
- **Runtime**: 108 ms
- **Memory**: 14.3 MB
- **Solution**: Sum the rows and perform an argsort.

### Problem 1339
- **Name**: Maximum Product of Splitted Binary Tree
- **Runtime**: 657 ms
- **Memory**: 74.9 MB
- **Solution**: The removing of 1 edge to make 2 subtrees is the same as comparing a subtree from a given node the the rest of the tree without it. So we can simply find the total sum of the tree recursively, then make another recursive traversal with all subtree sums and their differences with the rest of the tree.

### Problem 1342
- **Name**: Number of Steps to Reduce a Number to Zero
- **Runtime**: 37 ms
- **Memory**: 13.8 MB
- **Solution**: Directly implemented the process.

### Problem 1345
- **Name**: Jump Game IV
- **Runtime**: 665 ms
- **Memory**: 39.3 MB
- **Solution**: This is a simple shortest path problem without edge weights or an admissable heuristic, so we can just use BFS. However cases are made to make a simple BFS run quadratically. Using a 2-sided BFS actuall solves the problem very quickly. However a more proper solution is to use note that we can keep track of neighbor groups to not search them again, greatly cutting down the problem in general.

### Problem 1351
- **Name**: Count Negative Numbers in a Sorted Matrix
- **Runtime**: 142 ms
- **Memory**: 17.4 MB
- **Solution**: Simply iterate through the matrix, we can start in minimum corner and go up by rows, and break to a new row when we hit a non-negative column, and return entirely when we hit a non-negative start to a row.

### Problem 1356
- **Name**: Sort Integers by The Number of 1 Bits
- **Runtime**: 54 ms
- **Memory**: 16.5 MB
- **Solution**: We can using Python's build-in sorted function, with a custom key.

### Problem 1361
- **Name**: Validate Binary Tree Nodes
- **Runtime**: 271 ms
- **Memory**: 19.1 MB
- **Solution**: First find the root node, and check there are no other roots. Then search from the root node checking there are no cycles.

### Problem 1402
- **Name**: Reducing Dishes
- **Runtime**: 42 ms
- **Memory**: 13.8 MB
- **Solution**: Sort the satisfactions since we want the largest satisfaction to take advantage of the largest time multiplier. We then want to see which negative dishes we should drop. Use cumulative sum technique to get the effect of shifting down all future dishes by 1 by dropping a dish. We can then run through greedily checking if dropping the dish results in a net gain.

### Problem 1406
- **Name**: Stone Game III
- **Runtime**: 5431 ms
- **Memory**: 505.4 MB
- **Solution**: Use dynamic programming over the current position along the piles and the player's turn. A more efficient solution is to only keep track of the current and last 3 states for each player.

### Problem 1420
- **Name**: Build Array Where You Can Find The Maximum Exactly K Comparisons
- **Runtime**: 91 ms
- **Memory**: 16.5 MB
- **Solution**: Dymanic programming, moving forward over the array, and keeping track of the possible max values for each number of changes so far. If we go past the target number of changes, discard. Compute the number of ways to reach a new changes for a given max, as well as current change, use the accumulated sum so far to quickly compute the number of ways to reach new max. Also if staying the same then any value less than is good, so we multiply to get count.

### Problem 1424
- **Name**: Diagonal Traverse II
- **Runtime**: 784 ms
- **Memory**: 37.2 MB
- **Solution**: Notice that the effect of going along the diagonal is the same as shifting down each next column and then doing along, like a pyramid. So we can set up the pyramid to receive the entries apropriately and then traverse easily to give the result.

### Problem 1425
- **Name**: Constrained Subsequence Sum
- **Runtime**: 1517 ms
- **Memory**: 36 MB
- **Solution**: We can pass through nums once keeping track of the larges possible subsequence so far. If we encounter a non-negative number try to include it, if we encounter a string of negtive numbers keep track of the largest value possible to achieve a given position using a heap. A better solution is to use a monotonic queue.

### Problem 1441
- **Name**: Build an Array With Stack Operations
- **Runtime**: 48 ms
- **Memory**:16.3 MB
- **Solution**: We actually don't need to store the stack, since we'll never remove a value once it matches in target, and since both target and the stream are increasing we can only proceed forward, and each time we encounter a value from the stream we know isn't in target we can remove it immediately, making it a trivial march forward.

### Problem 1443
- **Name**: Minimum Time to Collect All Apples in a Tree.
- **Runtime**: 541 ms
- **Memory**: 49.2 MB
- **Solution**: Imagine all the apples moving up the tree until they reach the a node that has already been processed. We know each node takes 2s to move in then out, plus its descendants. We just need to parse the parents into an efficient format. This is the first time I've gotten "Beats 100%" on the timing.

### Problem 1444
- **Name**: Number of Ways of Cutting a Pizza
- **Runtime**: 291 ms
- **Memory**: 16 MB
- **Solution**: Dynamic programming. Since we always give away the upper and left sides of the pizza after a cut, we can keep track of the minimum x and y left, as well as the number of cuts left, making a triple we can cache. We also need a quick way of checking of a cut has as least one apple left in it, and if the remaining pizza has at least one apple left: we can do this with the cumulative sum technique, but in 2D.

### Problem 1456
- **Name**: Maximum Number of Vowels in a Substring of Given Length
- **Runtime**: 172 ms
- **Memory**: 18.5 MB
- **Solution**: This is a simple sliding window, which we can implement with a simple count of the vowels in the current window and update with each increment.

### Problem 1458
- **Name**: Max Dot Product of Two Subsequences
- **Runtime**: 568 ms
- **Memory**: 99 MB
- **Solution**: Classic dynamic programming with memoization. We go over indices of the two arrays and decide whether to use the pair in the dot product or carry forward searching other pairs.

### Problem 1466
- **Name**: Reorder Routes to Make All Paths Lead to the City Zero
- **Runtime**: 1282 ms
- **Memory**: 57.9 MB
- **Solution**: Take record of the graph and its complement. Perform BFS out from node 0 on the undirected graph, using the complement to help implement. At each edge check if it's in the original graph, and hence reached traveling outward from the origin: this is an edge the needs to be flipped.

### Problem 1470
- **Name**: Shuffle the Array
- **Runtime**: 57 ms
- **Memory**: 14.1 MB
- **Solution**: Used Python's list comprehension with proper indexing into the original array.

### Problem 1472
- **Name**: Design Browser History
- **Runtime**: 222 ms
- **Memory**: 16.4 MB
- **Solution**: Make an list to hold the urls, and extend it as needed with append. Use an index to keep place for the forward and backward history, and also keep an index for the maximum index after forward history is cleared: avoids reallocation.

### Problem 1489
- **Name**: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
- **Runtime**: 795 ms
- **Memory**: 16.5 MB
- **Solution**: Any MST we build will contain all critical edges, and will contain some of the pseudocritical edges. If an edge is in our original MST, then check if it's critical by attempting to build an MST without it (remember to check connectivity by checking a search will visit all nodes even without the edge). If an edge is not in our original MST, then check if it's pseudocritical by starting off building an MST with that edge already selected: use Kruskal's for this.

### Problem 1491
- **Name**: Average Salary Excluding the Minimum and Maximum Salary
- **Runtime**: 51 ms
- **Memory**: 16.2 MB
- **Solution**: Easy enough to do, just subtracted the max and min from the total sum, then divided by the length minus 2.

### Problem 1493
- **Name**: Longest Subarray of 1's After Deleting One Element
- **Runtime**: 325 ms
- **Memory**: 19.1 MB
- **Solution**: Just need to keep track of the length of the current and previous run of 1s. Appending a 0 to the array helps with edge cases, and the final case to catch is if the array is entirely 1s, since one has to be deleted: just check if it's the result is the length of the original array and if so decrement it.

### Problem 1498
- **Name**: Number of Subsequences That Satisfy the Given Sum Condition
- **Runtime**: 9238 ms
- **Memory**: 29.1 MB
- **Solution**: First thing to notice is the order of the numbers doesn't matter, because any subarray about a given minimum and maximum can be extended to contribute more numbers lower than the given max without changing violting the target. So we can sort, then run up over the minimums, and find a max that satisfied the condition, and take all subarrays within, which means a power of 2.

### Problem 1503
- **Name**: Last Moment Before All Ants Fall Out of a Plank
- **Runtime**: 156 ms
- **Memory**: 17.4 MB
- **Solution**: This is a classic problem in which we can notice that ants colliding are functionally the same as moving throught eachother, therefore we just have to find the max steps from the left and right arrays respectively.

### Problem 1512
- **Name**: Number of Good Pairs
- **Runtime**: 34 ms
- **Memory**: 16.4 MB
- **Solution**: This is just the number of unique pairs we can choose from the sets of same value. So we can solve this in a 1-liner with Python's Counter class and the comb math function.

### Problem 1519
- **Name**: Number of Nodes in the Sub-Tree With the Same Label
- **Runtime**: 3145 ms
- **Memory**: 183.9 MB
- **Solution**: Constructed the undirected graph, then performed DFS from the root, returning the sub-tree counts, and updating the solution array along the way. Careful of the undirected nature, and keep track of the parent, so as always search down in depth.

### Problem 1535
- **Name**: Find the Winner of an Array Game
- **Runtime**: 537 ms
- **Memory**: 30 MB
- **Solution**: We don't actually need to do the list updating, since we know our winner can only be increasing and numbers moved to the end can only be less than it. Therefore we just run through the numbers with pointers looking for k consecutive victories and if we reach the end of the list we know we'll win all remaining ones.

### Problem 1539
- **Name**: Kth Missing Positive Number
- **Runtime**: 51 ms
- **Memory**: 14 MB
- **Solution**: Besides the easy linear solution, we can do better with binary search to find the index at which the value shows k elements have been skipped so far. The answer is then that index+k.

### Problem 1547
- **Name**: Minimum Cost to Cut a Stick
- **Runtime**: 833 ms
- **Memory**: 20 MB
- **Solution**: Dynamic programming, memoizing over the left and right indices in the sorted cuts array. At each step we need to perform a cut between the left and right indices, and then search the sub-problems for their optimal solutions.

### Problem 1557
- **Name**: Minimum Number of Vertices to Reach All Nodes
- **Runtime**: 1191 ms
- **Memory**: 54.1 MB
- **Solution**: The nodes in questions are the ones with no parents. An easy way and efficient way to find this is start with the set of all nodes and remove all the nodes on the tail of each edge.

### Problem 1561
- **Name**: Maximum Number of Coins You Can Get
- **Runtime**: 511 ms
- **Memory**: 28.7 MB
- **Solution**: We should greedily choose the top 2 piles and bottom pile each round since we can never make a better choice. We can sort the array and slice of the bottom and skip every second element to get our coins.

### Problem 1572
- **Name**: Matrix Diagonal Sum
- **Runtime**: 119 ms
- **Memory**: 16.7 MB
- **Solution**: One pass to get both diagonals works, and checking if the square matrix is an odd size to remove the second use of the center element.

### Problem 1584
- **Name**: Min Cost to Connect All Points
- **Runtime**: 2133 ms
- **Memory**: 77.9 MB
- **Solution**: Since we are just worried about connectivity this is just the problem of finding the minimum spanning tree on the complete graph. Use Kruskal's with union-find.

### Problem 1601
- **Name**: Maximum Number of Achievable Transfer Requests
- **Runtime**: 2937 ms
- **Memory**: 16.4 MB
- **Solution**: This is a linear 0-1 optimization problem with equality contraints. Pretty sure this is NP-hard, so we have to do a brute-force check of all possibilities, which works for the problem's bounds. Interestingly this problem is equivalues to finding a set of disjoint cycles within the multi-graph of the greatest cumulative length.

### Problem 1603
- **Name**: Design Parking System
- **Runtime**: 139 ms
- **Memory**: 16.8 MB
- **Solution**: Simply keep track of the remainin spots for each parking space.

### Problem 1611
- **Name**: Minimum One Bit Operations to Make Integers Zero
- **Runtime**: 23 ms
- **Memory**: 16.3 MB
- **Solution**: The operations mentioned only change 1 bit at a time, but allow up to go up indefinitely or down to 0: this is the definition of counting up and down in Grey code.

### Problem 1615
- **Name**: Maximal Network Rank
- **Runtime**: 301 ms
- **Memory**: 18.7 MB
- **Solution**: We don't have to check all pairs and all edges, we only have to consider a few cases. The first is if there is more than 1 city with equally highest degree: we check all pair or a pair with no road between them, in which case these disjoint cities would make the maximal network rank, otherwise any pair works. If only 1 city has highest degree, then we look at every city with degree equal to the second highest degree to see if there's one not sharing a road with the highest, in which case that pair will be best otherwise any from the second highest degrees.

### Problem 1626
- **Name**: Best Team With No Conflicts
- **Runtime**: 397 ms
- **Memory**: 14.1 MB
- **Solution**: DP using an array mapping ages to max achievable scores results in the best performance. Go through the players in order of individual score, and this ensures we can slice our array to alwyas contain younger players scoring the same or less. Take the maximum of the slice each time, updating the best result so far in the array. The final result will be the best score in the array.

### Problem 1630
- **Name**: Arithmetic Subarrays
- **Runtime**: 170 ms
- **Memory**: 16.7 MB
- **Solution**: We can sort each of the sub-arrays and check that their contents has constant difference. We could use a set to be more efficient on the time complexity.

### Problem 1657
- **Name**: Determine if Two Strings Are Close
- **Runtime**: 347 ms
- **Memory**: 15.4 MB
- **Solution**: Since we can reorder all the letters, order doesn't matter, but we can't get or remove letters, so we need to check the sets match, also the counts of unique letters can't be changed (but we can change which letters they are) so those need to be compared as well, which can be done by sorting the counts before comparing.

### Problem 1658
- **Name**: Minimum Operations to Reduce X to Zero
- **Runtime**: 1059 ms
- **Memory**: 39 MB
- **Solution**: Used a prefix sum with a map to the index to find the minimum start and end indices to match the target.

### Problem 1662
- **Name**: Check If Two String Arrays are Equivalent
- **Runtime**: 52 ms
- **Memory**: 16.3 MB
- **Solution**: In python we can just join all the strings in the arrays and check if they are equal.

### Problem 1672
- **Name**: Richest Customer Wealth
- **Runtime**: 62 ms
- **Memory**: 13.8 MB
- **Solution**: Sum rows and take the max.

### Problem 1685
- **Name**: Sum of Absolute Differences in a Sorted Array
- **Runtime**: 675 ms
- **Memory**: 31.7 MB
- **Solution**: Since the array is sorted, we can use a cumulative sum to keep track of elements less than, and compute the sum of elements greater than a given element, and therefore compute the absolute values easily without negatives.

### Problem 1704
- **Name**: Determine if String Halves Are Alike
- **Runtime**: 61 ms
- **Memory**: 13.9 MB
- **Solution**: Simply run though the first and second halves of the string counting up vowels, then compare the counts from each side.

### Problem 1732
- **Name**: Find the Highest Altitude
- **Runtime**: 40 ms
- **Memory**: 16.3 MB
- **Solution**: Simply run through the list keeping track of the cumulative sum and maximum of its value.

### Problem 1743
- **Name**: Restore the Array From Adjacent Pairs
- **Runtime**: 914 ms
- **Memory**: 65 MB
- **Solution**: We can just build a map of each value to its adjacents, and then find one end by an entry that only has 1 neighbor. We then walk through to the other end.

### Problem 1751
- **Name**: Maximum Number of Events That Can Be Attended II
- **Runtime**: 912 ms
- **Memory**: 62.5 MB
- **Solution**: Because the way we get to an event doesn't matter, just our score, we can keep track of the max sore for each remaining k, then move forward by startDays, using a heap to keep track of trailing days we can move up.

### Problem 1759
- **Name**: Count Number of Homogenous Substrings
- **Runtime**: 117 ms
- **Memory**: 17.3 MB
- **Solution**: We can keep track of what the last seen character is and how many we've see so far. At we can makes homogenous substrings with any of the contigious matching characters and the most recently seen one too, so we just add the current count to the result.

### Problem 1793
- **Name**: Maximum Score of a Good Subarray
- **Runtime**: 877 ms
- **Memory**: 27.5 MB
- **Solution**: We start at index k and go down possible minimum values, expanding the array as possible and looking for possible maximum results.

### Problem 1799
- **Name**: Maximize Score After N Operations
- **Runtime**: 1171 ms
- **Memory**: 24.1 MB
- **Solution**: Dynamic programming recursively defined with caching. Precompute all the GCDs with Euclid's algorithm.

### Problem 1814
- **Name**: Count Nice Pairs in an Array
- **Runtime**: 547 ms
- **Memory**: 26.8 MB
- **Solution**: We can rearrange the equation to see we just need to compare differences in the original numbers with their reversed: so we can get counts of these differences and count how many pairs exist with the combination function.

### Problem 1822
- **Name**: Sign of the Product of an Array
- **Runtime**: 70 ms
- **Memory**: 16.4 MB
- **Solution**: Simply run through the numbers, noting a 0 will make the entire result 0, and only negative values change the result.

### Problem 1838
- **Name**: Frequency of the Most Frequent Element
- **Runtime**: 1158 ms
- **Memory**: 31.2 MB
- **Solution**: Use a sliding window to keep track of the window sum difference to the sum if every element was equal to the rightmost, this gives us how much needs to be incremented in the window to compare against k, and we can tighten the window as needed.

### Problem 1845
- **Name**: Seat Reservation Manager
- **Runtime**: 443 ms
- **Memory**: 43.9 MB
- **Solution**: Needing to have instant access to the smallest member and be able to return elements to the set, this is just a heap.

### Problem 1846
- **Name**: Maximum Element After Decreasing and Rearranging
- **Runtime**: 410 ms
- **Memory**: 26.3 MB
- **Solution**: Simply sort the array, and start with 0 ensuring we either meet a value in rannge of the previous, or bring it down to be one greater than the previous.

### Problem 1870
- **Name**: Minimum Speed to Arrive on Time
- **Runtime**: 2274 ms
- **Memory**: 30.5 MB
- **Solution**: We can do binary search. Start with lower bound of 1 and upper bound of speed that would make every train arrive in an hr. Watch out for edge cases.

### Problem 1877
- **Name**: Minimize Maximum Pair Sum in Array
- **Runtime**: 1009 ms
- **Memory**: 30.2 MB
- **Solution**: To minimize we should sum largest values with smallest values. So sort the array and pair the first half with the reversed second half.

### Problem 1887
- **Name**: Reduction Operations to Make the Array Elements Equal
- **Runtime**: 827 ms
- **Memory**: 23.7 MB
- **Solution**: Sort the array and run through it keeping track of number of unique values seen because that's the number of steps each value needs to take to reach the bottom.

### Problem 1921
- **Name**: Eliminate Maximum Number of Monsters
- **Runtime**: 744 ms
- **Memory**: 38.6 MB
- **Solution**: We can divide to get the time for each monster to arrive and check if we have the laser ready by seeing if there's any remainder.

### Problem 1930
- **Name**: Unique Length-3 Palindromic Subsequences
- **Runtime**: 1602 ms
- **Memory**: 17.2 MB
- **Solution**: Because we're only looking for length-3 palindromes we actually only have `26*26=676` possibilities. To find which ones were present efficiently we can find the first and last appearance of each letter and then run through the whole string once checking for middle letter candidates for our palindromes.

### Problem 1970
- **Name**: Last Day Where You Can Still Cross
- **Runtime**: 1493 ms
- **Memory**: 25.2 MB
- **Solution**: One will no longer be able to cross when the water connects the left and right sides. We can check connectivity faster than searching for paths, using union-find. Start off with extra columns on the left and right whose members make the left and right sets, and we check once those sets are merged.

### Problem 1980
- **Name**: Find Unique Binary String
- **Runtime**: 36 ms
- **Memory**: 16.2 MB
- **Solution**: We can do this efficiently using Cantor's diagonal argument. Simply run through the strings and take the flip of the ith bit from each, that way every string mismatches in at least one place.

### Problem 2009
- **Name**: Minimum Number of Operations to Make Array Continuous
- **Runtime**: 720 ms
- **Memory**: 35.3 MB
- **Solution**: Sort the array and remove duplicates. Because needing to move an element to the front is the same number of operations as moving an element to the end fo the continuous streak, we can choose an element already in the array to be the first one. How many elements would already be in its streak could be found using binary search to find where the last element would go, or its index if it is in the array currently. We use this the figure out how many remaining element need to be changed.

### Problem 2022
- **Name**: Convert 1D Array Into 2D Array
- **Runtime**: 1017 ms
- **Memory**: 21.4 MB
- **Solution**: Check the size first. Then simply slice the original array, using list comprehension to build the 2D array.

### Problem 2024
- **Name**: Maximize the Confusion of an Exam
- **Runtime**: 463 ms
- **Memory**: 18.8 MB
- **Solution**: Run through flipping answers as needed until k runs out, then reverse the first time used to try to keep the longest consecutive streak. Used a queue to keep track of last index, but a 2 pointer approach to the sliding window is more efficient.

### Problem 2038
- **Name**: Remove Colored Pieces if Both Neighbors are the Same Color
- **Runtime**: 125 ms
- **Memory**: 17.4 MB
- **Solution**: We can only remove letters that are in groups of 3 or more, so essentially we remove letters until we have pairs beside eachother or singles. Because of this we'll never join groups. So we just count the number of removable letters for each player and see if A has enough to outlast B.

### Problem 2050
- **Name**: Parallel Courses III
- **Runtime**: 1408 ms
- **Memory**: 45.6 MB
- **Solution**: Since we can take as many courses in parallel as we want we should always take a course as soon as possible as soon as we ahve finished all prereqs. We just need to check for new courses ready to take after completing a course. I used a heap to keep track of when the next course would be complete and it's time, thought it seems that isn't necessary.

### Problem 2130
- **Name**: Maximum Twin Sum of a Linked List
- **Runtime**: 972 ms
- **Memory**: 56.9 MB
- **Solution**: Put all the values in a list and then perform the twin sum there. A more space efficient method would be to reverse the second half of the list.

### Problem 2140
- **Name**: Solving Questions With Brainpower
- **Runtime**: 1754 ms
- **Memory**: 63.4 MB
- **Solution**: Classic dynamic programming since we can't go back on questions: we can compute the name score achievable by a given question.

### Problem 2147
- **Name**: Number of Ways to Divide a Long Corridor
- **Runtime**: 361 ms
- **Memory**: 17.5 MB
- **Solution**: The number of ways to divide the corridor is the product of the number of wall placements on each stretch of plants between each group of 2 seats. We can run through this pretty quickly counting strings of plants and total seats. Of course any hall with odd seats has no valid solutions.

### Problem 2187
- **Name**: Minimum Time to Complete Trips
- **Runtime**: 2331 ms
- **Memory**: 28.4 MB
- **Solution**: We know the rations of each bus used should be approximately equal to their reciprocal, however to find the exact value, we'll need to search to pin the value down. We can use binary search to cut down the search space exponentially.

### Problem 2215
- **Name**: Find the Difference of Two Arrays
- **Runtime**: 173 ms
- **Memory**: 16.7 MB
- **Solution**: We can do this easily with asymetric set difference.

### Problem 2225
- **Name**: Find Players With Zero or One Losses
- **Runtime**: 1911 ms
- **Memory**: 69.2 MB
- **Solution**: Simply count the losses for each player, and also keep track of winning players as existing. Sort at the end.

### Problem 2244
- **Name**: Minimum Rounds to Complete All Tasks
- **Runtime**: 1793 ms
- **Memory**: 28.5 MB
- **Solution**: Use Python's Counter class to get counts of each object, then if there's a 1 there's no solutions, otherwise take 3s until either 0, 2 or 4 are left, use modular arithmetic to check.

### Problem 2246
- **Name**: Longest Path With Different Adjacent Characters
- **Runtime**: 2430 ms
- **Memory**: 167.5 MB
- **Solution**: We can solve this with DFS, and handling the cases where there the longest path is in a sub-tree, or between two sub-paths, or is part of a larger path by returning both the longest overall path so far, as well as the longest path ending there.

### Problem 2251
- **Name**: Number of Flowers in Full Bloom
- **Runtime**: 901 ms
- **Memory**: 37.1 MB
- **Solution**: By sorting the arrays by time, we can go through person by person, and then see which flowers we haven't looked at yet have bloomed before looking at our current person. For each blooming flower be put its endtime in a heap, which we can then correct to only contain those still in bloom for the given person: the size of the heap is the nubmer of flowers still in bloom.

### Problem 2256
- **Name**: Minimum Average Difference
- **Runtime**: 1799 ms
- **Memory**: 24.8 MB
- **Solution**: Keep a current starting sum and ending sum, then take the means and round on the spot on each index, updating the result if necessary.

### Problem 2264
- **Name**: Count Nodes Equal to Average of Subtree
- **Runtime**: 50 ms
- **Memory**: 17.5 MB
- **Solution**: We can solve this with a recursive function returning the subtree sums, node counts and result.

### Problem 2305
- **Name**: Fair Distribution of Cookies
- **Runtime**: 4026 ms
- **Memory**: 16.4 MB
- **Solution**: Use a branch and bound search, keeping track of the best solution found so far to prune off branches of search paths which pass the limit.

### Problem 2306
- **Name**: Naming a Company
- **Runtime**: 657 ms
- **Memory**: 28.8 MB
- **Solution**: If we create maps from each starting letter to the set of their possible suffixes, then we can go through each pair of letters, and find the set intersection reasonably quickly, which will give us words that can't be used as pairs, all others can be used as pairs, so we can perform the multiplication quickly.

### Problem 2316
- **Name**: Count Unreachable Pairs of Nodes in an Undirected Graph
- **Runtime**: 2311 ms
- **Memory**: 81.7 MB
- **Solution**: Use a BFS to find all the connected components, then get their sizes. The number of pairs between any component is their sizes multiplied. A faster way of computing the multiplication of the sizes of every component is to use the match of expanding the brackets.

### Problem 2348
- **Name**: Number of Zero-Filled Subarrays
- **Runtime**: 1035 ms
- **Memory**: 24.7 MB
- **Solution**: We can solve this efficiently by just keeping track of the current streak of 0s, and when a streak is broken, add the triangluar number of the streak length (the number of start and end pairs within the streak) to the accumulated result.

### Problem 2352
- **Name**: Equal Row and Column Pairs
- **Runtime**: 652 ms
- **Memory**: 22.6 MB
- **Solution**: We only need to go over each row and column once if we use hashing. We can make a map of the hash of each row to its index, and for the each column, check if there are any matching rows.

### Problem 2359
- **Name**: Find Closest Node to Given Two Nodes
- **Runtime**: 2782 ms
- **Memory**: 44 MB
- **Solution**: Performed a DFS from each node to get a dict of the distances, stopping either at the leaf, or when a cycle is entered. Then take the min from the intersection of the dicts.

### Problem 2360
- **Name**: Longest Cycle in a Graph
- **Runtime**: 1194 ms
- **Memory**: 37.4 MB
- **Solution**: This is finding the largest strongly connected component in a graph. We don't need a full Tarjan's algorithm, because each node only has one edge: we just need to find the cycle in the chain. We can do so using a dict to keep track of which nodes are in the chain, and how far along they are. We can then instantly find cycle lengths when we find a cycle.

### Problem 2369
- **Name**: Check if There is a Valid Partition For The Array
- **Runtime**: 1217 ms
- **Memory**: 30.3 MB
- **Solution**: We can use a state-machine keeping track of all possible states we could be in running through the array just once and checking we're able to arrive at a valid end state.

### Problem 2390
- **Name**: Removing Stars From a String
- **Runtime**: 215 ms
- **Memory**: 15.6 MB
- **Solution**: This can be solved easily with a stack. Run through the string adding characters to the stack, and for stars pop from the stack.

### Problem 2391
- **Name**: Minimum Amount of Time to Collect Garbage
- **Runtime**: 1040 ms
- **Memory**: 39.4 MB
- **Solution**: We send out end truck independently and keep track of potential travel time, but only add it once we reach a house with the right type of garbage, and reset the counter.

### Problem 2405
- **Name**: Optimal Partition of String
- **Runtime**: 187 ms
- **Memory**: 14.6 MB
- **Solution**: The greedy approach should be used, scanning through the string and only putting breaks each time a duplicate in the current section is found. Duplicates can be found quickly with a set. Since we know the set will at most contain 26 elements we can use a constant length binary array.

### Problem 2418
- **Name**: Sort the People
- **Runtime**: 265 ms
- **Memory**: 14.5 MB
- **Solution**: Use Python's zip to combind the lists, then they can be sorted together, and finish by only returning the names.

### Problem 2419
- **Name**: Longest Subarray With Maximum Bitwise AND
- **Runtime**: 2658 ms
- **Memory**: 28.5 MB
- **Solution**: AND operations can never increase Hamming weight, only decrease of stay the same. Therefore it's a matter of counting streaks of values equal to the max of the array, and finding the longest streak.

### Problem 2420
- **Name**: Find All Good Indices
- **Runtime**: 1060 ms
- **Memory**: 30.7 MB
- **Solution**: Create first differences array, then use a sliding window to count when the window contains all preceding non-increasing and proceding non-decreasing. This allows us to grab all the good indices. Careful for off-by-one errors.

### Problem 2427
- **Name**: Number of Common Factors
- **Runtime**: 31 ms
- **Memory**: 13.9 MB
- **Solution**: The bound for this problem are small enough we can just run through all numbers from 1 to the minimum number (inclusive) checking the mod with both.

### Problem 2428
- **Name**: Maximum Sum of an Hourglass
- **Runtime**: 528 ms
- **Memory**: 16.6 MB
- **Solution**: Simple brute for summations over every possible index.

### Problem 2429
- **Name**: Minimize XOR
- **Runtime**: 63 ms
- **Memory**: 14 MB
- **Solution**: First find the Hamming weight of the num2, then first cancel out as many leading 1s from num1 as possible, and assign any leftover 1s to the lowest 0s possible.

### Problem 2433
- **Name**: Find The Original Array of Prefix Xor
- **Runtime**: 639 ms
- **Memory**: 36.4 MB
- **Solution**: We just need to find which value will xor to become the next in pref, and since xor is its own inverse that makes it easy. Just start with a value of 0.

### Problem 2439
- **Name**: Minimize Maximum of Array
- **Runtime**: 747 ms
- **Memory**: 26.8 MB
- **Solution**: The operation doesn't change the sum of the array, only moves value down, and accumulates at the 0 index. Therefore we can decrease any element except for the 0 element. So we can choose that element to take on value so as to always be the max in the array. From here was can run through the array, knowing we can alaways spread out the sum so far if ever we find values greater than the 0 index, and we should increase the 0 index as needed so as to always be the largest in the array.

### Problem 2441
- **Name**: Largest Positive Integer That Exists With Its Negative
- **Runtime**: 251 ms
- **Memory**: 14 MB
- **Solution**: Make a set from nums to instantly look up if a negative is present, then filter the list, add -1 to the final set, and take the max remaining value.

### Problem 2442
- **Name**: Count Number of Distinct Integers After Reverse Operations
- **Runtime**: 1056 ms
- **Memory**: 41 MB
- **Solution**: With Python we can simply convert to string and reverse and convert back to int. Finish by using set to get only distinct elements.

### Problem 2443
- **Name**: Sum of Number and Its Reverse
- **Runtime**: 6738 ms
- **Memory**: 13.8 MB
- **Solution**: While one could math/logic it out for a much faster solution, a brute force search (barely) works.

### Problem 2444
- **Name**: Count Subarrays With Fixed Bounds
- **Runtime**: 847 ms
- **Memory**: 28.7 MB
- **Solution**: We can solve this problem by first noticing that any values outside the min-max range will effectively "chop" the array into pieces independant from eachother. We can run through any of these pieces of the array and consider all the valid sub-arrays ending on our given index: these will be distinct from other indices, and the number of valid subarray starts will stretch from either the start or the last out-of-bounds element up to the last appearance of either the min or max element, whichever comes first. Using this we can compute the result in linear time with constant memory.

### Problem 2455
- **Name**: Average Value of Even Numbers That Are Divisible by Three
- **Runtime**: 198 ms
- **Memory**: 14.1 MB
- **Solution**: This is another way of saying all numbers divisible by 6, so just filter the list, and handle the case where the list is empty before returning the mean.

### Problem 2456
- **Name**: Most Popular Video Creator
- **Runtime**: 849 ms
- **Memory**: 64.9 MB
- **Solution**: Use Python's Counter to aggregate the total views for each creator, then filter down to only the top count, then grab the top vids for each creator and finish off by formatting the output.

### Problem 2457
- **Name**: Minimum Addition to Make Integer Beautiful
- **Runtime**: 79 ms
- **Memory**: 13.9 MB
- **Solution**: Search for the solution by adding to each digit until we reach it's complement, checking if the digits sum is below the target. This way we work our way up digit by digit until we reach the optimal solution.

### Problem 2458
- **Name**: Height of Binary Tree After Subtree Removal Queries
- **Runtime**: 2791 ms
- **Memory**: 162 MB
- **Solution**: We can find heights of the binary tree with nodes deleted by storing all the solutions from 2 passes, and then querying that cache. The first pass returns the greatest depth below each node, the second passes down information about the greatest depth without anything below the given node.

### Problem 2466
- **Name**: Count Ways To Build Good Strings
- **Runtime**: 331 ms
- **Memory**: 20.2 MB
- **Solution**: Dynamic programming counting the number of ways to get a given length, then summing in the range.

### Problem 2477
- **Name**: Minimum Fuel Cost to Report to the Capital
- **Runtime**: 2214 ms
- **Memory**: 178.8 MB
- **Solution**: Because of the tree structure we can use a DFS approach to compute the fuel needed to get the current city and how many representatives will need to pass through that city, and we can then compute the number of cars needed to reach the next city. 

### Problem 2483
- **Name**: Minimum Penalty for a Shop
- **Runtime**: 186 ms
- **Memory**: 21.4 MB
- **Solution**: Using a cumulative sum we can instantly compute the penalty for any index, and quickly find the minimum.

### Problem 2492
- **Name**: Minimum Score of a Path Between Two Cities
- **Runtime**: 1619 ms
- **Memory**: 82.1 MB
- **Solution**: Careful, this isn't a shortest path problem: instead just use a graph search to find the shortest edge in the connected component of the graph.

### Problem 2542
- **Name**: Maximum Subsequence Score
- **Runtime**: 1110 ms
- **Memory**: 37.8 MB
- **Solution**: The challenge is deciding if an element is worth adding to the subsequence even if it lowers the min because its sum value is large. If we order the pairs of number starting with the highest multipliers and continue descending we can evaluate each pair's effect on the result to see if it's worth adding. We can then maintain the numbers added to the sum in a heap.

### Problem 2544
- **Name**: Alternating Digit Sum
- **Runtime**: 51 ms
- **Memory**: 13.9 MB
- **Solution**: Usual approach to extracting digits: modular arithmetic and integer division. After that it's trivial to swap the signs of digits running from the most significant, and sum for the final result.

### Problem 2545
- **Name**: Sort the Students by Their Kth Score
- **Runtime**: 492 ms
- **Memory**: 20.5 MB
- **Solution**: Since we are sorting by rows, we can easily use Python's sorted function with a lambda function key.

### Problem 2546
- **Name**: Apply Bitwise Operations to Make Strings Equal
- **Runtime**: 44 ms
- **Memory**: 15.1 MB
- **Solution**: If we perform the analysis on what we can transform pairs of bits into, we can see that we can use 1s as a pivot to turn any other bit into a either a 1 or a 0. This means if our target has no 1s in it then we can only reach it if we start off with no 1s, and otherwise we can reach any target so long as we start off with at least one 1.

### Problem 2547
- **Name**: Minimum Cost to Split an Array
- **Runtime**: 6534 ms
- **Memory**: 14.1 MB
- **Solution**: Step forward through the array, keeping track of the optimal cost for any split on the previous elements. Then look forward assuming a final split was made here and update for the minimum possible future costs. The overall minimum cost will then be the final result in the dynamic programming array.

### Problem 2642
- **Name**: Design Graph With Shortest Path Calculator
- **Runtime**: 685 ms
- **Memory**: 19.4 MB
- **Solution**: While the Floyd–Warshall algorithm for all pairs shortest path comes to mind, and might allow for some effciencies in recomputing updates to the shorest paths once updated, however based on the number of calls to the shorest path method, it seems that just re-running Dijkstra's algorithm is the way to go.

### Problem 2707
- **Name**: Extra Characters in a String
- **Runtime**: 144 ms
- **Memory**: 16.9 MB
- **Solution**: Well want to work our way through the string finding the fewest possible leftover characters to arrive at a given position until we reach the end. From a position we can see which future position we can reach with a word in the dictionary efficiently using a trie.

### Problem 2742
- **Name**: Painting the Walls
- **Runtime**: 2110 ms
- **Memory**: 436.5 MB
- **Solution**: Dynamic programming over the index of the wall considered and the remaining time needed to cover all the walls. Min of including vs excluding cases.

### Problem 2785
- **Name**: Sort Vowels in a String
- **Runtime**: 149 ms
- **Memory**: 19.8 MB
- **Solution**: Filter out the vowels into their own list to sort, and make a queue/stack to pop from, then rerun through the original string and either use the original consonant or the new sorted vowel. A better solution asymptotically is to use counting sort since the cardinality of vowels is low and a constant.

### Problem 2788
- **Name**: Split Strings by Separator
- **Runtime**: 122 ms
- **Memory**: 16.4 MB
- **Solution**: Python's already let's us split string by a delimiter, and we can use list comprehension to get a flattened list. Finally an if statement will filter out empty strings.

### Problem 2789
- **Name**: Largest Element in an Array after Merge Operations
- **Runtime**: 1008 ms
- **Memory**: 27.2 MB
- **Solution**: Since all numbers are positive, might as well perform the operation on the furthest right as much as possible since it can only lead to larger numbers. Treat it like a stack.

### Problem 2815
- **Name**: Max Pair Sum in an Array
- **Runtime**: 145 ms
- **Memory**: 16.4 MB
- **Solution**: We can use the string representation of numbers to get each digit and then find the max. We can then use this to quickly group our sets of equal max digits. From there we just check all pairs for the maximum value.

### Problem 2816
- **Name**: Double a Number Represented as a Linked List
- **Runtime**: 1675 ms
- **Memory**: 22.3 MB
- **Solution**: For the contest I just convertted directly to an int and then back. A proper solution is to first reverse the linked list, perform the arithmetic, then reverse once more.

### Problem 2843
- **Name**: Count Symmetric Integers
- **Runtime**: 900 ms
- **Memory**: 16.4 MB
- **Solution**: Brute force checking every number using string casting and slicing.

### Problem 2844
- **Name**: Minimum Operations to Make a Special Number
- **Runtime**: 48 ms
- **Memory**: 16.3 MB
- **Solution**: Basically we have only a few cases to cover: ending with 00,25,50,75. Write a whole bunch of cases, looking to delete numbers from the end to reach either the ending in 5 or ending in 0 cases.

### Problem 2845
- **Name**: Count of Interesting Subarrays
- **Runtime**: 905 ms
- **Memory**: 34.7 MB
- **Solution**: We can compute once which elements of the array have the remainder criterion, now we need to count sub-arrays whose sum also meet the criterion. Since it's a sub-array sum we're interested in we can use the cumulative sum, and a counter to get all the counts of matching end of each array positon that will meet the criterion.

### Problem 2873
- **Name**: Maximum Value of an Ordered Triplet I
- **Runtime**: 57 ms
- **Memory**: 16.2 MB
- **Solution**: Since the problem size is small enough, just did a double loop for pairs, using and accumulated max from proceeding elements to get the maximum triplet.

### Problem 2874
- **Name**: Maximum Value of an Ordered Triplet II
- **Runtime**: 923 ms
- **Memory**: 29.9 MB
- **Solution**: Since the problem size is now large we need to be cleverer. To get the maximum value for any given j, we want to maximize the value from the i and the k, and since there are guaranteed to be on the left and right sides respectively we can just use a left and right cumulative maximum array for each.

### Problem 2875
- **Name**: Minimum Size Subarray in Infinite Array
- **Runtime**: 442 ms
- **Memory**: 49.5 MB
- **Solution**: If the target is greater than the sum of the array, then we'll clearly need to repeat it until the target is less: therefore we can use division and mod to get to this point. Afterwards we can simply double the array size and look for the smallest subarray for the target, using the cumulative sum technique.

### Problem 2876
- **Name**: Count Visited Nodes in a Directed Graph
- **Runtime**: 1489 ms
- **Memory**: 47.2 MB
- **Solution**: This is simular to finding lengths of cycles in linked lists. For each node we knows we'll eventually find a cycles, so search until a cycles is detected, easily done with a set, though more efficient is a tortoise-hare algorithm. I also used a stack to get the distances of other nodes in the list to the cycle. In this way we only visit each node a few times at most.

### Problem 2849
- **Name**: Determine if a Cell Is Reachable at a Given Time
- **Runtime**: 40 ms
- **Memory**: 16.18 MB
- **Solution**: We can add any number of steps on top of the shortest path. Since we have diagonals available to us the shortest path is the smaller of the x and y distances. One edge case is if we start in the same position as the target and time is 1, we cannot succeed because we need to step off first.

### Problem 2946
- **Name**: Matrix Similarity After Cyclic Shifts
- **Runtime**: 122 ms
- **Memory**: 16.33 MB
- **Solution**: We can interate over each row and check that all numbers would be equal after a cyclic shift using modular arithmetic. We can do left and right shifting by a sign change depending on parity of the row number. Break early if any mismatch found.

### Problem 2947
- **Name**: Count Beautiful Substrings I
- **Runtime**: 1701 ms
- **Memory**: 16.26 MB
- **Solution**: For this problem's bounds we can simply iterate over ends and then each paired start, keeping a running track of the number of vowels seen on the end, and for the start so we immediately know the number of vowels and consonents for each substring.

### Problem 2948
- **Name**: Make Lexicographically Smallest Array by Swapping Elements
- **Runtime**: 1188 ms
- **Memory**: 51.04 MB
- **Solution**: By transitivity, we can find chains of numbers which can swap places arbitrarily, so we just need to find these chained groups by sorting and keeping track of the original indices. We then places the sorted values into the indices available for the group.

## Resources
- Blind 75 problem set: https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
- Sean Prashad's LeetCode patterns: https://github.com/SeanPrashad/leetcode-patterns
