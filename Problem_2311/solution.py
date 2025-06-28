class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = int(s, 2)
        mask = 1
        while mask << 1 <= value:
            mask <<= 1
        result = len(s)
        for d in s:
            if value <= k:
                return result
            if d == '1':
                result -= 1
                value &= ~mask
                while mask > value:
                    mask >>= 1
        return result


