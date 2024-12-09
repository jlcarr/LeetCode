class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        lastinv = [0]
        lastinvi = 0
        for i,(p,pp) in enumerate(zip(nums[1:],nums[:-1])):
            if p%2 == pp%2:
                lastinvi = i+1
            lastinv.append(lastinvi)
        #print(lastinv)
        return [lastinv[qt] <= qf for qf,qt in queries]
            
