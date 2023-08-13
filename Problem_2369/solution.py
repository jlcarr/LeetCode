class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        states = [[True], [False], [False,False], [False,False]]
        for i,v in enumerate(nums):
            new_states = [[False], [False], [False,False], [False,False]]
            if states[0][0]:
                new_states[1][0] = True
                new_states[2][0] = True
                new_states[3][0] = True
            if states[1][0] and nums[i-1] == v:
                new_states[0][0] = True
            if states[2][0] and nums[i-1] == v:
                new_states[2][1] = True
            if states[2][1] and nums[i-1] == v:
                new_states[0][0] = True
            if states[3][0] and nums[i-1]+1 == v:
                new_states[3][1] = True
            if states[3][1] and nums[i-1]+1 == v:
                new_states[0][0] = True
            states = new_states
            if not any([any(s) for s in states]):
                return False
        return states[0][0]
