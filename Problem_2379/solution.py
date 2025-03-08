class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        result = k
        for i,v in enumerate(blocks):
            count += v == 'B'
            if i >= k:
                count -= blocks[i-k] == 'B'
            result = min(result, k-count)
        return result
