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

### Problem 234
- **Name**: Palindrome Linked List
- **Runtime**: 932 ms
- **Memory**: 46.5 MB
- **Solution**: I just converted to list and compared reverse. O(1) space is possible by first counting the middle position, then reversing the second half, and walking through both comparing.

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

