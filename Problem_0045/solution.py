class Solution:
    def jump(self, nums: List[int]) -> int:
        min_cost = dict()
        min_cost[0] = 0
        for i in range(len(nums)-1):
            #print(min_cost)
            cost = min_cost[i]
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    if i+j not in min_cost:
                        min_cost[i+j] = cost + 1
                    else:
                        min_cost[i+j] = min(min_cost[i+j], cost + 1)
        return min_cost[len(nums)-1]
