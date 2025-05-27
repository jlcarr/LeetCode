from collections import Counter
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        G = {i: set() for i in range(len(colors))}
        Ginv = {i: set() for i in range(len(colors))}
        for i,j in edges:
            G[i].add(j)
            Ginv[j].add(i)
        
        # keep counts on each node
        counts = {i: Counter(colors[i]) for i in range(len(colors))}
        # remove roots and merge counts down, taking maxes
        roots = [i for i,js in Ginv.items() if not js]
        #print(roots)
        while roots:
            i = roots.pop()
            for j in G[i]:
                Ginv[j].remove(i)
                if not Ginv[j]:
                    roots.append(j)
                counts[j] |= counts[i] + Counter(colors[j])
        # check for cycle
        if any(Ginv.values()):
            return -1
        #print(counts)
        # when a leaf is reached, evaluate
        return max(c for cs in counts.values() for c in cs.values())
