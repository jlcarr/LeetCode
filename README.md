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
 
### Problem 133
- **Name**: Clone Graph
- **Runtime**: 71 ms
- **Memory**: 14.3 MB
- **Solution**: DFS, keeping a dictionary from node values to their copies.
 
### Problem 139
- **Name**: Word Break
- **Runtime**: 45 ms
- **Memory**: 15 MB
- **Solution**: Make a trie of the dictionary words, then ran through the string looking for trie leaves, and when one is found, add the next possible starting point to a heap to continue the search. This is also solveable by just keeping an array the length of the string to represent valid possible starting points and then for each get all next possible starting points.
 
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
 
### Problem 148
- **Name**: Sort List
- **Runtime**: 1121 ms
- **Memory**: 36.5 MB
- **Solution**: We can use mergesort to solve this problem. The lists lend themselves nicely to merging, however finding the midpoints requires 2 run-throughs at each step to find the middle node and split.
 
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
 
### Problem 162
- **Name**: Find Peak Element
- **Runtime**: 51 ms
- **Memory**: 14 MB
- **Solution**: Use binary search: on each new midpoint check to see if it's increasing or decreasing, then pull up the left or right bound accordinly to tighten in on a peak.
 
### Problem 169
- **Name**: Majority Element
- **Runtime**: 264 ms
- **Memory**: 15.6 MB
- **Solution**: Python's collections class makes this problem easy to solve in 1 line. However it is O(n) space, while an O(1) space solution exists via the Boyer-Moore voting algorithm:
 
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
 
### Problem 226
- **Name**: Invert Binary Tree
- **Runtime**: 65 ms
- **Memory**: 13.9 MB
- **Solution**: Recusively call the function on each node's children, and swap the results.
 
### Problem 230
- **Name**: Kth Smallest Element in a BST
- **Runtime**: 51 ms
- **Memory**: 18 MB
- **Solution**: DFS, returning the count of children so that a given node in the BST knows how many smaller elements there are, using a global boolean to indicate success and break out returning the solution.
 
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

### Problem 338
- **Name**: Counting Bits
- **Runtime**: 80 ms
- **Memory**: 20.7 MB
- **Solution**: By removing the most significant binary digit we can a smaller number that has already been computed. As such we can run through the values onces and check previous solutions fill out the answer.

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

### Problem 383
- **Name**: Ransom Note
- **Runtime**: 85 ms
- **Memory**: 14.2 MB
- **Solution**: Used the collections.Counter datastructure, which is essentially a multi-set, and comes with an 'inclusion' operator.

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

### Problem 442
- **Name**: Find All Duplicates in an Array
- **Runtime**: 854 ms
- **Memory**: 21.7 MB
- **Solution**: Since all values are supposed to be positive use negating an int at a given index as a marker of already having seen it.

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

### Problem 494
- **Name**: Target Sum
- **Runtime**: 366 ms
- **Memory**: 14.2 MB
- **Solution**: My initial solution was a simple recursive DP over the number we're looking at and the current target. However this solution is not optimal since it will memoize all the possible values of target for every step. A more optimal solution is to iterate over the numbers we either add of subtract to the target and create a new cache from the value at that given step, discarding the older cache as it's no longer needed.

### Problem 543
- **Name**: Diameter of Binary Tree
- **Runtime**: 66 ms
- **Memory**: 16.4 MB
- **Solution**: Recursively find max depths by recursing on children, then the max path is max sum of max depths between children for any node.

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

### Problem 698
- **Name**: Partition to K Equal Sum Subsets
- **Runtime**: 161 ms
- **Memory**: 14 MB
- **Solution**: This is essentially a decision problem version of the bin packing problem. Being NP-Complete, we need to perform an exhaustive search, taking each element and tryig to place it in each of the bins, but we can speed things up be exiting early if no solution is found. We can also notice we'll want to place an element in a bin as soon as possible: we should never end up with the case where we choose to skip over placing an element in a bin which is still empty: the element should have either been already placed in a non-empty bin to keep building it, or placed in the empty to to start it: never just leave a bin empty.

### Problem 704
- **Name**: Binary Search
- **Runtime**: 290 ms
- **Memory**: 15.5 MB
- **Solution**: Classic binary search algorithm: use a left and right pointer, then check if the middle value is greather than or lesser than the target values and update the left and right pointers to the middle value accordingly to tighen the bounds until a solution is found.

### Problem 713
- **Name**: Subarray Product Less Than K
- **Runtime**: 1642 ms
- **Memory**: 16.6 MB
- **Solution**: This is a classic 2-pointer, which both monotonically increase, because the product can only increase. Increase the right pointer until a value less than k is found, set the left pointer there two, then increase the right pointer, accumulating to the product until it can't anymore, then increase the left pointer, dividing out of the accumulated product.

### Problem 720
- **Name**: Longest Word in Dictionary
- **Runtime**: 142 ms
- **Memory**: 14.5 MB
- **Solution**: First sort the words by lexicographic order, then run through, keeping a set of the buildable words found so far. If a word's substring is in the buildable, then it too is, and we can also check if it is greater in length than the current best.

### Problem 767
- **Name**: Reorganize String
- **Runtime**: 33 ms
- **Memory**: 13.9 MB
- **Solution**: Use Python's Counter to get frequencies. Use the most frequent element to make buckets of adjacent characters, which we can then run over placing each new character in the next bucket. We're guarunteed to have at least 1 character between each of the same type.

### Problem 784
- **Name**: Letter Case Permutation
- **Runtime**: 62 ms
- **Memory**: 14.6 MB
- **Solution**: Run through all letters of the string, checking if lowercase and uppercase are different, if so double the result size and append the lowercase to the first half and uppercase the second half, otherwise just append to all.

### Problem 828
- **Name**: Count Unique Characters of All Substrings of a Given String
- **Runtime**: 3426 ms
- **Memory**: 14.7 MB
- **Solution**: Solve this problem by counting the number of substrings in which a given letter appears once: summing over all letters is the same as summing the lengths of all substrings with unique letters. For each letter run through the string keeping track of the last position the character was seen, and the distance to the previous sighting of the character before that. We can update the result whenever a new sighting is found by counting the pairs of choices between indices before and including the previous sighting with the indices after the previous sighting (including none), which can be computed by a simple multiplication. This allows for a single pass for each letter.

### Problem 844
- **Name**: Backspace String Compare
- **Runtime**: 30 ms
- **Memory**: 14 MB
- **Solution**: Build up resulting strings literally: pop the end whenever a backspace character is encountered, then compare the 2.

### Problem 863
- **Name**: All Nodes Distance K in Binary Tree
- **Runtime**: 71 ms
- **Memory**: 14.4 MB
- **Solution**: Two parts: search down to find the target node, then return back up with distance remaining. Recurse down again at each node to grab the relevant nodes.

### Problem 876
- **Name**: Middle of the Linked List
- **Runtime**: 47 ms
- **Memory**: 13.9 MB
- **Solution**: Ran through the list once to count, then again up to the middle.

### Problem 895
- **Name**: Maximum Frequency Stack
- **Runtime**: 540 ms
- **Memory**: 23 MB
- **Solution**: The max frequency can only change by at most 1 on a given operation, so keep track of its value, then have a map of values to their frequencies, then frequencies to stack. That way when popped the max frequency can be found and most recent returned, and for a value it's frequency and be found quickly and incremented and added to the next frequency stack.

### Problem 904
- **Name**: Fruit Into Baskets
- **Runtime**: 1280 ms
- **Memory**: 20.1 MB
- **Solution**: Since only 2 types are allowed, we only need to look for continuguous streaks of 2 types. We can run through the array once, and keep track of the 2 types currently under consideration and the last time each type was seen. Upon a new type we discard the other that isn't adjacent, and reupdate the length of our current streak.

### Problem 973
- **Name**: K Closest Points to Origin
- **Runtime**: 1730 ms
- **Memory**: 18.3 MB
- **Solution**: One easy method is to compute all the distances and perform and argsort on the result. Interesting to note KD trees are also a useful datastructure of such problems. Quickselect would probably be the fastest, though a heap is also quite fast.

### Problem 986
- **Name**: Interval List Intersections
- **Runtime**: 204 ms
- **Memory**: 14.9 MB
- **Solution**: Two pointers running through the two lists, checking for interval overlaps, and then adding the overlappign interval to the result (overlapping interval will be the max of both starts, and the mins of boths ends: i.e. the intersection). If there's no overlap the earliest starting one is incremented to catch up, if there is overlap the soonest ending one is incremented to check for more overlaps.

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

### Problem 2022
- **Name**: Convert 1D Array Into 2D Array
- **Runtime**: 1017 ms
- **Memory**: 21.4 MB
- **Solution**: Check the size first. Then simply slice the original array, using list comprehension to build the 2D array.

### Problem 2251
- **Name**: Richest Customer Wealth
- **Runtime**: 62 ms
- **Memory**: 13.8 MB
- **Solution**: Sum rows and take the max.

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

## Resources
- Blind 75 problem set: https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
- Sean Prashad's LeetCode patterns: https://github.com/SeanPrashad/leetcode-patterns
