class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # construct graph
        G = {i:set() for i in range(n)}
        for e in edges:
            G[e[0]].add(e[1])
            G[e[1]].add(e[0])
        
        # start with leaves
        q = [i for i,es in G.items() if len(es) == 1]
        
        while True:
            if len(q) == 1 or (len(q) == 2 and q[0] in G[q[1]]):
                return list(q)
            new_q = []
            for i in q:
                # remove self from graph
                for e in G[i]:
                    G[e].remove(i)
                    # if we have a new leaf, queue it
                    if len(G[e]) == 1:
                        new_q.append(e)
                del G[i]
            q = new_q
