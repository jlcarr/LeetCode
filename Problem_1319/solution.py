class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        G = {i:set() for i in range(n)}
        for cs,ct in connections:
            G[cs].add(ct)
            G[ct].add(cs)
        unsearched = set(range(n))
        components = 0
        excess = 0
        while unsearched:
            curr = unsearched.pop()
            component = {curr}
            q = [curr]
            while q:
                curr = q.pop()
                for neighbor in G[curr]:
                    if neighbor not in component:
                        q.append(neighbor)
                        component.add(neighbor)
                    else:
                        excess += 1
                    G[neighbor].remove(curr)
                del G[curr]
            unsearched -= component
            components += 1
        if excess >= components-1:
            return components-1
        return -1
