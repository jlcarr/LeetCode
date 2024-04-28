from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [1,1]
        # construct tree
        G = defaultdict(set)
        for a,b in edges:
            if a not in G:
                G[a] = set()
            G[a].add(b)
            if b not in G:
                G[b] = set()
            G[b].add(a)

        desc = defaultdict(set)
        desc_num = defaultdict(int)
        desc_sum = defaultdict(int)

        anc = dict()
        anc_sum = defaultdict(int)

        # contract leaves
        leaves = [k for k,v in G.items() if len(v) == 1]

        while leaves:
            curr = leaves.pop()
            # remove
            parent = G[curr].pop()
            del G[curr] # empty
            G[parent].remove(curr)
            # add
            desc[parent].add(curr)
            desc_num[parent] += 1 + desc_num[curr]
            desc_sum[parent] += 1 + desc_num[curr] + desc_sum[curr]
            anc[curr] = parent
            # new leaf
            if len(G[parent]) == 1:
                leaves.append(parent)
            if len(G) == 2:
                break

        roots = list(G.keys())
        #print(roots)
        anc_sum[roots[0]] = 1 + desc_num[roots[1]] + desc_sum[roots[1]]
        anc_sum[roots[1]] = 1 + desc_num[roots[0]] + desc_sum[roots[0]]
    
        while roots:
            curr = roots.pop()
            for i in desc[curr]:
                roots.append(i)
                # anc + otherdesc +
                #print(curr, i, anc_sum[curr], desc_sum[curr] - (1 + desc_num[i] + desc_sum[i]), n - (1 + desc_num[i]))
                anc_sum[i] = anc_sum[curr]
                anc_sum[i] += desc_sum[curr] - (1 + desc_num[i] + desc_sum[i])
                anc_sum[i] += n - (1 + desc_num[i])
        #print(desc_num)
        #print(desc_sum)
        #print(anc_sum)
        return [desc_sum[i]+anc_sum[i] for i in range(n)]

