class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        complete_nums = sorted([(n,i) for i,l in enumerate(nums) for n in l])
        
        result = [complete_nums[0][0], complete_nums[-1][0]]
        
        counts = [0] * len(nums)
        l,r = 0,-1
        while r+1 < len(complete_nums):
            # cast out r
            while r+1 < len(complete_nums) and not all(counts):
                r += 1
                # get all of value
                curr_r,from_list = complete_nums[r]
                counts[from_list] += 1
                while r+1 < len(complete_nums) and complete_nums[r+1][0] == curr_r:
                    r += 1
                    counts[complete_nums[r][1]] += 1
            # real in l
            while all(counts) and l < r:
                # update current solution
                curr_l,from_list = complete_nums[l]
                if curr_r - curr_l < result[-1] - result[0]:
                    result = [curr_l,curr_r]
                
                # get all of value
                curr_l,from_list = complete_nums[l]
                counts[from_list] -= 1
                while l+1 < len(complete_nums) and complete_nums[l+1][0] == curr_l:
                    l += 1
                    counts[complete_nums[l][1]] -= 1
                l += 1

        return result
