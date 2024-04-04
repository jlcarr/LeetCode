class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            result = max(result,count)
        return result
