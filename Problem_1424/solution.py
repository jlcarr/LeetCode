class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        acc = []
        for i,row in enumerate(nums):
            for j, val in enumerate(row):
                if len(acc) <= i + j:
                    acc.append([])
                acc[i+j].append(val)
        
        return [val for stack in acc for val in reversed(stack)]
