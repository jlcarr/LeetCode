from collections import Counter, defaultdict
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # get all modulo sets
        modsets = defaultdict(list)
        for i in nums:
            modsets[i%k].append(i)
        result = 1
        # find all subset
        for v in modsets.values():
            withit = 1
            withoutit = 0
            prev = -k
            counts = Counter(v)
            for i in sorted(counts.keys()):
                if i-k == prev:
                    withit, withoutit = ((1<<counts[i])-1)*withoutit, withit+withoutit
                else:
                    withit, withoutit = ((1<<counts[i])-1)*(withit+withoutit), (withit+withoutit)
                #print(i, withit, withoutit, counts[i], (1<<counts[i])-1)
                prev = i
            # multiply indpendent modulo set, subtract 1 for empty set
            result *= withit + withoutit
        return result - 1
