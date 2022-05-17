class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        constraining_heights = []
        heights.append(0)
        for i, h in enumerate(heights):
            while constraining_heights and constraining_heights[-1][1] >= h:
                j, possible_max_height = constraining_heights.pop()
                width = i 
                if constraining_heights:
                    width -= constraining_heights[-1][0]+1
                result = max(result, possible_max_height*width)
            constraining_heights.append((i,h))            
            
        return result
