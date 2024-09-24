class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefs = dict()
        for x in arr1:
            stack = []
            while x > 0:
                stack.append(x % 10)
                x //= 10
            curr = prefs
            while stack:
                if stack[-1] not in curr:
                    curr[stack[-1]] = dict()
                curr = curr[stack.pop()]
        
        result = 0
        for y in arr2:
            stack = []
            while y > 0:
                stack.append(y % 10)
                y //= 10
            curr = prefs
            subresult = 0
            while stack and stack[-1] in curr:
                subresult += 1
                curr = curr[stack.pop()]
            result = max(result, subresult)
        
        return result
