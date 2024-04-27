from functools import cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        #unique
        ss = []
        prev = ''
        for c in s:
            if c != prev:
                ss.append(c)
                prev = c
        s = ''.join(ss)

        pos = dict()
        for i,c in enumerate(s+'\n'):
            if c not in pos:
                pos[c] = []
            pos[c].append(i)
        
        @cache
        def dp(l,r):
            if l > r:
                return 0
            result = 1 + dp(l+1,r)
            c = s[l]
            for m in pos[c]:
                if l < m <= r:
                    result = min(result, dp(l,m-1)+dp(m+1,r))
            return result

        return dp(0, len(s)-1)
