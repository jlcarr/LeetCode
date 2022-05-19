import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_zeroes = sum([i == 0 for i in nums])
        if n_zeroes >= 2:
            return [0] * len(nums)
        if n_zeroes == 1:
            prod = 1
            for i in nums:
                if i != 0:
                    prod *= i
            return [prod if i == 0 else 0 for i in nums]
        
        negs = [i < 0 for i in nums]
        odd_negs = sum(negs) % 2
        nums = [abs(i) for i in nums]
        # negs odd_negs
        # T T -> +
        # T F -> -
        # F T -> -
        # F F -> +
        #print(negs, odd_negs)
        
        result = [math.log(i) for i in nums]
        prod = sum(result)
        result = [round(math.exp(prod-i)) for i in result]
        result = [i if s == odd_negs else -i for s,i in zip(negs,result)]
        return result
        
