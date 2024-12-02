class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pos = {v:i for i,v in enumerate(arr)}
        for i,v in enumerate(arr):
            d = v<<1
            if d in pos and pos[d] != i:
                return True
        return False
