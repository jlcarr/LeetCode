class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums.append(0)
        curr_count = nums[0].bit_count()
        prev_max = -2
        curr_max = nums[0]
        curr_min = curr_max
        for i in nums:
            #print(i, i.bit_count())
            if i.bit_count() != curr_count:
                #print(i, curr_min, prev_max)
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_max = i
                curr_min = i
                curr_count = i.bit_count()
            else:
                curr_min = min(curr_min, i)
                curr_max = max(curr_max, i)
            #print(i, curr_count, curr_max, curr_min, prev_max)
        return True
