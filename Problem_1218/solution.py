class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        counts = dict()
        for n in arr:
            if n in counts:
                if n+difference in counts:
                    counts[n+difference] = max(counts[n+difference], 1 + counts[n])
                else:
                    counts[n+difference] = 1 + counts[n]
            else:
                counts[n+difference] = 1
        return max(counts.values())
