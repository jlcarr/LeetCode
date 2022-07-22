class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        targets = {0:1}
        for n in nums:
            new_targets = dict()
            for t,count in targets.items():
                if t+n not in new_targets:
                    new_targets[t+n] = 0
                new_targets[t+n] += count
                if t-n not in new_targets:
                    new_targets[t-n] = 0
                new_targets[t-n] += count
            targets = new_targets
        if target not in targets:
            targets[target] = 0
        return targets[target]
