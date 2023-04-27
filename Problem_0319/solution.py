import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        # [1,2,2,3,2,4,2,4,3,4,2,5,2,4,4,5]
        # [1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5]
        return int(math.sqrt(n))
        
