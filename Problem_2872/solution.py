class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # absorb leaves in with num divisible component and remainder
        # for a single node, given a set of leaf remainders, zeros split, others must merge

        if n == 1:
            return 1

        G = dict()
        for a,b in edges:
            if a not in G:
                G[a] = set()
            G[a].add(b)
            if b not in G:
                G[b] = set()
            G[b].add(a)

        leaves = []
        for i in range(n):
            if len(G[i]) == 1:
                leaves.append(i)

        result = 1 # for the final node

        while leaves:
            l = leaves.pop()
            if not G[l]: #final node
                break

            # remove leaf
            parent = G[l].pop()
            del G[l]
            G[parent].remove(l)

            # add parent if new leaf
            if len(G[parent]) == 1:
                leaves.append(parent)

            # propagate
            if values[l] % k == 0:
                result += 1
            values[parent] += values[l] % k
            #print(l, parent, result, values, leaves)
        
        return result
