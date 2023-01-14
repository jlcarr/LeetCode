class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # use union-find to get the equivalent sets
        # find the lex-min of each set, and craft dict of each char to min
        # apply transformation to the baseStr
        unionfind = list(range(26))
        def find(c):
            if c != unionfind[c]:
                unionfind[c] = find(unionfind[c])
            return unionfind[c]

        def union(c1,c2):
            p1,p2 = find(c1), find(c2)
            if p1 < p2:
                unionfind[p2] = p1
            elif p2 < p1:
                unionfind[p1] = p2

        a = ord('a')
        for c1,c2 in zip(s1,s2):
            union(ord(c1)-a, ord(c2)-a)
        
        return ''.join(chr(find(ord(c)-a)+a) for c in baseStr)

