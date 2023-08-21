class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # for each edge make an mst regular, then if included make one without, otherwise make one starting with.
        # using kruskals

        # if first with is mst, and second wihtout not mst, then critical
        # if first is mst, and second without is mst, then pseudocritical
        # if not first, and second with is mst, then pseudocritical
        # if not first, and second with is not mst, then none

        G = {i:set() for i in range(n)}
        for e in edges:
            G[e[0]].add(e[1])
            G[e[1]].add(e[0])

        sortedEdges = sorted(range(len(edges)), key=lambda e: edges[e][2])
        #print(sortedEdges)

        # create any MST
        anycriticals = set([])
        self.unionfind = list(range(n))
        mstWeight = 0
        for ie in sortedEdges:
            a,b,w = edges[ie]
            if self.union(a,b):
                mstWeight += w
                anycriticals.add(ie)
        #print(mstWeight, anycriticals)

        criticals = []
        pseudocriticals = []
        for ie in sortedEdges:
            a,b,w = edges[ie]
            # first check connectivity
            q = [0]
            searched = set(q)
            while q:
                curr = q.pop()
                for adj in G[curr]:
                    if adj not in searched and not ((curr,adj) == (a,b) or (adj,curr) == (a,b)):
                        searched.add(adj)
                        q.append(adj)
            if len(searched) != n:
                criticals.append(ie)
                continue


            if ie in anycriticals:
                # create MST without
                self.unionfind = list(range(n))
                mstWithoutWeight = 0
                for ie2 in sortedEdges:
                    a2,b2,w2 = edges[ie2]
                    if ie2 == ie:
                        continue
                    if self.union(a2,b2):
                        mstWithoutWeight += w2
                        #print("\t",ie2, True, mstWithoutWeight)
                    #else:
                        #print("\t",ie2, False, mstWithoutWeight)
                #print(ie, ie in anycriticals, mstWithoutWeight, self.unionfind)
                if mstWithoutWeight == mstWeight:
                    pseudocriticals.append(ie)
                else:
                    criticals.append(ie)
            else:
                # create MST with
                self.unionfind = list(range(n))
                self.union(a,b)
                mstWithWeight = w
                for ie2 in sortedEdges:
                    a2,b2,w2 = edges[ie2]
                    if self.union(a2,b2):
                        mstWithWeight += w2
                #print(ie, ie in anycriticals, mstWithWeight)
                if mstWithWeight == mstWeight:
                    pseudocriticals.append(ie)
        return [criticals, pseudocriticals]

    def find(self, c):
        if c != self.unionfind[c]:
            self.unionfind[c] = self.find(self.unionfind[c])
        return self.unionfind[c]
    
    def union(self, c1,c2):
        p1,p2 = self.find(c1), self.find(c2)
        if p1 == p2:
            return False
        if p1 < p2:
            self.unionfind[p2] = p1
        elif p2 < p1:
            self.unionfind[p1] = p2
        return True
