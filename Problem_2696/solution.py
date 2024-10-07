class Solution:
    def minLength(self, s: str) -> int:
        result = 0
        stack = []
        for c in s:
            result += 1
            if c == 'A' or c == 'C':
                stack.append(c)
                continue
            if stack:
                if c == 'B' and stack[-1] == 'A' \
                    or c == 'D' and stack[-1] == 'C':
                    stack.pop()
                    result -= 2
                else:
                    stack = []
        return result
