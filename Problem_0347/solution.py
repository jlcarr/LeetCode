from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        for n,count in counts.items():
            buckets[count-1].append(n)
        return [n for bucket in buckets for n in bucket][-k:]
        
