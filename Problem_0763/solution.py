class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        orda = ord('a')
        firsts = [-1] * 26
        lasts = [-1] * 26
        for i,c in enumerate(s):
            ordc = ord(c)-orda
            if firsts[ordc] == -1:
                firsts[ordc] = i
            lasts[ordc] = i

        rs = [(i,j) for i, j in zip(firsts,lasts) if i != -1]
        rs.sort()
        #print(rs)

        result = []
        icurr = 0
        jcurr = 0
        for i,j in rs:
            if i > jcurr:
                result.append(jcurr+1-icurr)
                icurr = i
            jcurr = max(jcurr,j)
        result.append(len(s)-icurr)
        return result
        
