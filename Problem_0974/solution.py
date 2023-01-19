from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modsumcounts = Counter()
        modsumcounts[0] += 1
        result = 0
        acc = 0
        for i in nums:
            acc = (acc+i)%k
            result += modsumcounts[acc]
            modsumcounts[acc] += 1
        return result

