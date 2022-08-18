class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1 = []
        for c in s:
            if c == '#':
                if r1:
                    r1.pop()
            else:
                r1.append(c)
        r2 = []
        for c in t:
            if c == '#':
                if r2:
                    r2.pop()
            else:
                r2.append(c)
        return r1 == r2
