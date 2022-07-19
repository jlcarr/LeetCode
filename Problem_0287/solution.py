class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First find the point in the cycle
        tortoise = 0
        hare = 0
        while tortoise != hare or tortoise == 0:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]    
            
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return tortoise
        
        # The first point 0 is guarunteed to be outside the cycle we find because no element can map to 0
        
