class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        wcount = 0
        for i,c in enumerate(s):
            if c == '0':
                result += i - wcount
                wcount += 1
        return result
