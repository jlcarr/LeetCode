class Solution:
    def checkValidString(self, s: str) -> bool:
        stackMax = 0
        stackMin = 0
        for c in s:
            if c == '(':
                stackMax += 1
                stackMin += 1
            if c == ')':
                stackMax -= 1
                stackMin -= 1
            if c == '*':
                stackMax += 1
                stackMin -= 1
            if stackMax < 0:
                return False
            stackMin = max(0,stackMin)
        return stackMin == 0
            
