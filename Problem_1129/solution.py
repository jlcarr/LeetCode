from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # setup
        Gred = dict()
        for e0,ef in redEdges:
            if e0 not in Gred:
                Gred[e0] = set()
            if ef not in Gred:
                Gred[ef] = set()
            Gred[e0].add(ef)
        
        Gblue= dict()
        for e0,ef in blueEdges:
            if e0 not in Gblue:
                Gblue[e0] = set()
            if ef not in Gblue:
                Gblue[ef] = set()
            Gblue[e0].add(ef)

        # BFS
        q = deque([(0,True), (0,False)])
        dists = {n:0 for n in q}
        while q:
            node, color = q.pop()
            d = dists[(node, color)]
            neighbors = Gred.get(node, set()) if color else Gblue.get(node, set())
            for e in neighbors:
                if (e, not color) not in dists:
                    q.appendleft((e, not color))
                    dists[(e, not color)] = d+1
        
        #print(dists)
        result = [
            min(
                dists.get((i,True), n*n),
                dists.get((i,False), n*n)
            ) for i in range(n)]
        result = [i if i < n*n else -1 for i in result]

        return result
            
