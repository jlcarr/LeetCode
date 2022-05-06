class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remaining_jump = 1
        for p in nums[:-1]:
            remaining_jump -= 1
            remaining_jump = max(remaining_jump, p)
            if remaining_jump == 0:
                return False
        return True
