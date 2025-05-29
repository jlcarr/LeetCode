from collections import defaultdict
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # transitive property of even set
        # just 2-color tree for 2 sets
        # then for each node self set size + largest other set size
        # special case for both size 1
        if not edges1 and not edges2:
            return [0]

        # process 1
        G1 = defaultdict(set)
        for i,j in edges1:
            G1[i].add(j)
            G1[j].add(i)
        
        colors1 = {0: False}
        q = [0]
        while q:
            curr = q.pop()
            for child in G1[curr]:
                if child not in colors1:
                    colors1[child] = not colors1[curr]
                    q.append(child)
        counts1 = [len(colors1) - sum(colors1.values())]
        counts1.append(len(colors1) - counts1[0])
        counts1 = [counts1[colors1[i]] for i in range(len(colors1))]

        #print(counts1)

        # process 2
        G2 = defaultdict(set)
        for i,j in edges2:
            G2[i].add(j)
            G2[j].add(i)

        colors2 = {0: False}
        q = [0]
        while q:
            curr = q.pop()
            for child in G2[curr]:
                if child not in colors2:
                    colors2[child] = not colors2[curr]
                    q.append(child)
        max2 = sum(colors2.values())
        max2 = max(max2, len(colors2) - max2)
        #print(colors2)
        #print(max2)
        
        return [v + max2 for v in counts1]
