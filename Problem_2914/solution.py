class Solution:
    def minChanges(self, s: str) -> int:
        result = 0
        curr = s[0]
        count = 0
        for c in s:
            if c != curr: # break in streak
                if count % 2: # need to change current
                    result += 1
                else: # current substring is good
                    count = 0
                    curr = c
            count += 1
        return result
            

