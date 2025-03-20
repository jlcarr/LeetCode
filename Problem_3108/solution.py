class Solution:
    def find(self, i):
        if self.arr[i] == i:
            return i
        result = self.find(self.arr[i])
        self.arr[i] = result
        return result

    def union(self, i, j, w):
        i_root = self.find(i)
        j_root = self.find(j)
        newcost = self.cost[i_root] & self.cost[j_root] & w
        self.arr[max(i_root,j_root)] = min(i_root,j_root)
        self.cost[min(i_root, j_root)] = newcost

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.arr = list(range(n))
        self.cost = [-1] * n
        for u,v,w in edges:
            self.union(u,v,w)
        
        return [self.cost[self.find(s)] if self.find(s) == self.find(t) else -1 for s,t in query] 
            
