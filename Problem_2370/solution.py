class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        maxl = [0]*26
        for i,c in enumerate(s):
            vc = ord(c) - ord('a')
            curr = 0
            for pc in range(26):
                if abs(vc-pc) <= k:
                    curr = max(curr, maxl[pc])
            maxl[vc] = curr + 1
        return max(maxl)
