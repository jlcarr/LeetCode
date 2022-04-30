class Solution:
    def longestValidParentheses(self, s: str) -> int:
        popped = [False]*len(s)
        stack = []
        for i,p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif stack:
                pair_index = stack.pop()
                popped[pair_index] = True
                popped[i] = True
            #print(stack)
            #print(popped)
        max_streak = 0
        curr_streak = 0
        for v in popped:
            if v:
                curr_streak +=1
            else:
                max_streak = max(max_streak, curr_streak)
                curr_streak = 0
        max_streak = max(max_streak, curr_streak)
                
        return max_streak
