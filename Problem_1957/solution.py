class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        pp, p = '', ''
        for c in s:
            if c != pp or c != p:
                result.append(c)
            pp = p
            p = c
        return ''.join(result)
