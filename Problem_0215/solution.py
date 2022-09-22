import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        
        def partition(l, r, i_pivot):
            pivot = nums[i_pivot]
            nums[i_pivot], nums[r] = nums[r], nums[i_pivot]
            i_swap = l
            for i in range(l,r):
                if nums[i] > pivot:
                    nums[i_swap], nums[i] = nums[i], nums[i_swap]
                    i_swap += 1
            nums[i_swap], nums[r] = nums[r], nums[i_swap]
            return i_swap
            
        def quickselect(l, r):
            while True:
                if l == r:
                    return nums[l]
                i_pivot = random.randint(l,r)
                i_pivot = partition(l, r, i_pivot)

                #print(nums)
                if i_pivot == k:
                    return nums[k]
                elif i_pivot > k:
                    r = i_pivot - 1
                else:
                    l = i_pivot + 1

        return quickselect(0, len(nums)-1)
