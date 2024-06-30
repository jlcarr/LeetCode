class UF:
    def __init__(self, n):
        self.arr = list(range(n))
    def find(self, i):
        #print('find', i)
        if self.arr[i] == i:
            return i
        result = self.find(self.arr[i])
        self.arr[i] = result
        return result
    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root < j_root:
            self.arr[j_root] = i_root
        elif i_root > j_root:
            self.arr[i_root] = j_root
        return min(i_root, j_root)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = [(e[1]-1,e[2]-1) for e in edges if e[0] == 1]
        bob = [(e[1]-1,e[2]-1) for e in edges if e[0] == 2]
        both = [(e[1]-1,e[2]-1) for e in edges if e[0] == 3]
        e_count = 0
        # attempt prims with 3
        both_uf = UF(n)
        for u,v in both:
            if both_uf.find(u) != both_uf.find(v):
                both_uf.union(u,v)
                e_count += 1
        # complete alice with type 1
        a_uf = UF(0)
        a_uf.arr = both_uf.arr[:]
        for u,v in alice:
            if a_uf.find(u) != a_uf.find(v):
                a_uf.union(u,v)
                e_count += 1
        if not all(a_uf.find(0) == a_uf.find(i) for i in range(n)):
            return -1
        # complete bob with type 2
        b_uf = UF(0)
        b_uf.arr = both_uf.arr[:]
        for u,v in bob:
            if b_uf.find(u) != b_uf.find(v):
                b_uf.union(u,v)
                e_count += 1
        if not all(b_uf.find(0) == b_uf.find(i) for i in range(n)):
            return -1
        return len(edges) - e_count

