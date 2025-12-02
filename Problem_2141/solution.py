class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # it is optimal to run all batteries equally and share charge.
        # if there is a battery with more charge than the mean
        # then it might as well run 1 for the whole time
        # we can ignore it and look at the remaining
        batteries.sort()
        tot = sum(batteries)
        while batteries[-1] > tot // n:
            tot -= batteries.pop()
            n -= 1
        
        return tot//n
