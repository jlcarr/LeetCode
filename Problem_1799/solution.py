from collections import Counter
from functools import cache
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        counts = Counter(nums)
        n2 = len(nums)
        gcds = {}
        for i in range(n2):
            for j in range(i+1,n2):
                if (nums[i], nums[j]) in gcds:
                    continue
                a,b = nums[j], nums[i]
                while b != 0:
                    t = b
                    b = a % b
                    a = t
                gcds[(nums[i], nums[j])] = a
        print(gcds)
        
        @cache
        def rec(state):
            if not state:
                return 0
            result = 0
            n_temp = len(state)
            for i in range(n_temp):
                for j in range(i+1,n_temp):
                    v1,v2 = state[i], state[j]
                    temp = list(state)
                    temp.remove(v1)
                    temp.remove(v2)
                    temp = rec(tuple(temp))
                    result = max(result, n_temp * gcds[(v1,v2)] // 2 + temp)
                    #print(state, v1,v2, gcds[(v1,v2)], temp, result)
            #print(state, result)
            return result

        return rec(tuple(nums))
        
