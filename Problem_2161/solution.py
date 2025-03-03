class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt,eq,gt = [],[],[]
        for v in nums:
            if v < pivot:
                lt.append(v)
            elif v > pivot:
                gt.append(v)
            else:
                eq.append(v)
        return lt + eq + gt

