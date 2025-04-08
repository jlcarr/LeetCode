from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        #print(counts)
        ndist = sum(c > 1 for c in counts.values())
        i = 0
        while ndist > 0:
            i += 1
            for j in range(3*(i-1), min(len(nums), 3*i)):
                v = nums[j]
                counts[v] -= 1
                if counts[v] == 1:
                    ndist -= 1
            #print(counts)
        return i
