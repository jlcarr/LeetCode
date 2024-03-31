from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        tight_counts = Counter()
        tight_lp = 0
        large_counts = Counter()
        large_l = 0
        result = 0
        for r,n in enumerate(nums):
            # add next to windows
            tight_counts[n] += 1
            large_counts[n] += 1
            # ensure large window is in compliance
            while len(large_counts) > k:
                large_counts[nums[large_l]] -= 1
                if large_counts[nums[large_l]] == 0:
                    del large_counts[nums[large_l]]
                large_l += 1
            # tighten the tight window to 1 past
            while len(tight_counts) >= k:
                tight_counts[nums[tight_lp]] -= 1
                if tight_counts[nums[tight_lp]] == 0:
                    del tight_counts[nums[tight_lp]]
                tight_lp += 1
            if len(large_counts) == k:
                result += tight_lp-large_l
        return result
