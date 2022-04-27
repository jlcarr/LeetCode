class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        L, R = 0, len(height)-1
        while L < R:
            curr = min(height[L], height[R]) * (R - L)
            result = max(result, curr)
            if height[L] < height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
            else:
                if height[L+1] < height[R-1]:
                    R -= 1
                else:
                    L += 1
        
        return result
