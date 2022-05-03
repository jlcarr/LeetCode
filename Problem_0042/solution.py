class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        
        # find the max and it's last position
        max_height = max(height)
        last_max_index = 0
        for i,h in enumerate(height):
            if h == max_height:
                last_max_index = i
        #print(last_max_index, max_height)
        # anything less will hold water
        
        # find enpoints
        L = 0
        while L+1 < len(height) and height[L] <= height[L+1]:
            L = L+1
        R = len(height)-1
        while R > L and height[R-1] >= height[R]:
            R = R-1
        #print(L,R)
        
        # catch left-side and middle
        curr_height = height[L]
        i = L+1
        while i < last_max_index:
            if height[i] > curr_height:
                curr_height = height[i]
            result += curr_height - height[i]
            i += 1
            
        # catch right-side
        curr_height = height[R]
        i = R-1
        while i > last_max_index:
            if height[i] > curr_height:
                curr_height = height[i]
            result += curr_height - height[i]
            i -= 1
        
        return result
