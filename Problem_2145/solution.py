import itertools
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        acc = list(itertools.accumulate(differences))
        #print(acc)
        r = max(*acc, 0) - min(*acc, 0)
        return max(upper+1 - lower - r, 0)
        
