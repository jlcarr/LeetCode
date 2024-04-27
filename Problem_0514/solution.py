class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        l = len(ring)
        pos = dict()
        for i,c in enumerate(ring):
            if c not in pos:
                pos[c] = []
            pos[c].append(i)
        #print(pos)

        prevs = [(0,0)] # i pos -> cost
        for c in key:
            currs = []
            for i in pos[c]:
                costmin = prevs[0][1] + l + 1
                for j,cost in prevs:
                    costmin = min(costmin, cost + 1 + min(abs(i-j), l-abs(i-j)))
                currs.append((i,costmin))
            prevs = currs
            #print(c, prevs)
        return min([i[1] for i in prevs])

