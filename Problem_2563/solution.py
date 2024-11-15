class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Easier is to count the number of pairs <= upper
        # Then do the same thing for lower, and subract that off

        nums.sort()
        result = 0
        j_lower, j_upper = len(nums)-1, len(nums)-1
        for i in range(len(nums)):
            while i < j_lower and nums[i] + nums[j_lower] >= lower:
                j_lower -= 1
            while i < j_upper and nums[i] + nums[j_upper] > upper:
                j_upper -= 1
            result += max(0, j_upper-i) - max(0, j_lower-i)

        return result
