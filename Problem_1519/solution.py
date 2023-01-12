from collections import Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        G = dict()
        for e in edges:
            if e[0] not in G:
                G[e[0]] = set()
            if e[1] not in G:
                G[e[1]] = set()
            G[e[0]].add(e[1])
            G[e[1]].add(e[0])
        
        sol = [0]*n
        def rec(curr, parent):
            res = Counter()
            for e in G[curr]:
                if e != parent:
                    res += rec(e, curr)
            res[labels[curr]] += 1
            sol[curr] = res[labels[curr]]
            return res
        rec(0,-1)
        return sol
