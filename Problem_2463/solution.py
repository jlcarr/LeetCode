from functools import cache
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        maxv = 1 + len(robot) * max(abs(robot[0] - factory[-1][0]), abs(robot[-1] - factory[0][0]))

        @cache
        def dp(i, j, k):
            if i == len(robot):
                return 0
            if j == len(factory):
                return maxv
            result = dp(i, j + 1, 0)
            if factory[j][1] > k:
                result = min(result, dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]))
            return result
        
        return dp(0, 0, 0)
