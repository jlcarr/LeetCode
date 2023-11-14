class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firsts = dict()
        lasts = dict()
        for i,c in enumerate(s):
            if c not in firsts:
                firsts[c] = i
            lasts[c] = i
        
        middles = {k:set() for k in firsts.keys()}
        for i,c in enumerate(s):
            for k in firsts.keys():
                if i > firsts[k] and i < lasts[k]:
                    middles[k].add(c)
        
        return sum(len(s) for s in middles.values())
