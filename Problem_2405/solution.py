class Solution:
    def partitionString(self, s: str) -> int:
        counts = [0]*26
        result = 1
        for c in s:
            i = ord(c)-ord('a')
            if counts[i] > 0:
                result += 1
                counts = [0]*26
            counts[i] += 1
        return result
