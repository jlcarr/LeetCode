class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prevprev = cost[0]
        prev = cost[1]
        for i in range(2, n):
            prev, prevprev = cost[i] + min(prev, prevprev), prev
        return min(prev,prevprev)
