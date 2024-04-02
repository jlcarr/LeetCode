class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        invmapping = {}
        for c1,c2 in zip(s,t):
            if c1 not in mapping and c2 not in invmapping:
                mapping[c1] = c2
                invmapping[c2] = c1
            elif c1 not in mapping or mapping[c1] != c2:
                return False
        return True
