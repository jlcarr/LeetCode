class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        l,r = 0,len(letters)-1
        while l+1<r:
            m = (r+l)//2
            if letters[m] <= target:
                l = m
            else:
                r = m
        return letters[r]
        
