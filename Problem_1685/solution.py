class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)
        tot = sum(nums)
        acc = 0
        result = []
        for i,n in enumerate(nums):
            result.append((tot-acc) - (l-i)*n + i*n - acc)
            acc += n
        
        return result
