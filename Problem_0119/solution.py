import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [
            math.factorial(rowIndex) // (math.factorial(rowIndex-i) * math.factorial(i)) 
            for i in range(rowIndex+1)
        ]
