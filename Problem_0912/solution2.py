class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r = len(nums)//2, len(nums)
        while r > 1:
            if l > 0:
                l -= 1 # insert the next element
            else:
                r -= 1
                nums[0],nums[r] = nums[r],nums[0]

            root = l # sift down into the heap
            while 2*root+1 < r:
                child = 2*root+1
                if child+1 < r and nums[child] < nums[child+1]:
                    child += 1 # use a right child if greater
                if nums[root] < nums[child]:
                    nums[root],nums[child] = nums[child],nums[root]
                    root = child
                else:
                    break
        return nums
