from collections import Counter
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mask_counts = Counter()
        for row in matrix:
            key = tuple([v^row[0] for v in row])
            mask_counts[key] += 1
        return max(mask_counts.values())
