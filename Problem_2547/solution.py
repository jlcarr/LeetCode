from collections import Counter
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # run over all indices
        # assume we have a split there
        # run over future splits and post in optimal cost so far
        # max val is cost of split on every element
        cost_sofar = [k * len(nums) + len(nums)] * (len(nums)+1)
        cost_sofar[0] = 0
        
        # try cutting to exclude
        for i,n in enumerate(nums):
            already = Counter()
            already[n] += 1
            cost = cost_sofar[i] + k
            for j in range(i+1, len(nums)+1):
                cost_sofar[j] = min(cost_sofar[j], cost)
                if j == len(nums):
                    continue
                already[nums[j]] += 1
                if already[nums[j]] == 2:
                    cost += 2
                elif already[nums[j]] > 2:
                    cost += 1
        #print(cost_sofar)
        return(cost_sofar[-1])
        
        
