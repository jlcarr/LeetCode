class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        l = len(s)
        for istart in range(l):
            matched = True
            for i in range(l):
                if s[(istart + i)%l] != goal[i]:
                    matched = False
                    break
            if matched:
                return True
        return False
