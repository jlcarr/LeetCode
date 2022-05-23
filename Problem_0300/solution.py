class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        streak_mins = []
        
        for n in nums:
            i = len(streak_mins) -1 
            while i >= 0:
                if streak_mins[i] < n:
                    if i == len(streak_mins)-1:
                        streak_mins.append(n)
                    elif streak_mins[i+1] > n:
                        streak_mins[i+1] = n
                i -= 1
            if len(streak_mins) == 0:
                streak_mins.append(n)
            streak_mins[0] = min(streak_mins[0], n)
                
        return len(streak_mins)
