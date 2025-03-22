from collections import Counter
class Solution:
    def find(self, i):
        if self.arr[i] != i:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def union(self, i,j):
        i_root = self.find(i)
        j_root = self.find(j)
        self.arr[max(i_root, j_root)] = min(i_root, j_root)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.arr = list(range(n))
        edgecount = [0] * n
        for a,b in edges:
            edgecount[a] += 1
            edgecount[b] += 1
            self.union(a,b)
        for i in range(n):
            self.find(i)
        component_sizes = Counter(self.arr)
        iscomplete = {i:True for i,root in enumerate(self.arr) if i==root}
        #print(self.arr)
        #print(component_sizes)
        #print(edgecount)
        for i,root in enumerate(self.arr):
            iscomplete[root] = iscomplete[root] and (edgecount[i]+1 == component_sizes[root]) 
        return sum(iscomplete.values())
