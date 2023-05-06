class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        tail = len(nums)-1
        for head in range(len(nums)):
            while (head <= tail) and (nums[head] + nums[tail] > target):
                tail -= 1
            if head <= tail and nums[head] + nums[tail] <= target:
                result += 2**(tail-head)
                result %= 10**9 + 7
        return result
