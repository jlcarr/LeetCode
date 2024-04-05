class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if result and result[-1] != c and result[-1].upper() == c.upper():
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
