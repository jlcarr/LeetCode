from collections import Counter
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counts = Counter([0])
        for v in nums:
            for subsetv,count in list(counts.items()):
                counts[subsetv | v] += count
        return counts.most_common(1)[0][1]
