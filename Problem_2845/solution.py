from collections import Counter
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        result = 0
        counts = Counter()
        counts[0] += 1
        cumsum = 0
        for num in nums:
            cumsum = (cumsum + int(num % modulo == k)) % modulo
            # want cumsum - target = k (modulo)
            #target = (cumsum - k + modulo) % modulo
            target = (cumsum - k + modulo) % modulo
            result += counts[target]
            #print(result, num, cumsum, target, counts)
            counts[cumsum] += 1
            
        return result
