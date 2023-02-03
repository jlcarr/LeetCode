class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # 00 -> 00
        # 01 -> 11
        # 10 -> 11
        # 11 -> 10
        ones_s = s.count('1')
        ones_target = target.count('1')
        
        if ones_target == 0:
            return ones_s == 0
        
        return ones_s > 0
