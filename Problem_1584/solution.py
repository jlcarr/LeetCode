class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        self.unionfind = list(range(n))

        edges = [
            (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) 
            for i in range(n) for j in range(i)]
        edges.sort()
        #print(edges)

        # Kruskal's
        result = 0
        for cost,v1,v2 in edges:
            if self.union(v1, v2):
                #print(cost,v1,v2)
                result += cost
                #print(self.unionfind)
        return result
            

    def find(self, v):
        if self.unionfind[v] != v:
            self.unionfind[v] = self.find(self.unionfind[v])
        return self.unionfind[v]
            
    def union(self, v1, v2):
        set1, set2 = self.find(v1), self.find(v2)
        if set1 == set2:
            return False
        if set1 < set2:
            self.unionfind[set2] = set1
        else:
            self.unionfind[set1] = set2
        return True
