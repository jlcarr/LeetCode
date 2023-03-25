class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        G = {i:set() for i in range(n)}
        for a,b in edges:
            G[a].add(b)
            G[b].add(a)
        components = []
        unsearched = set(range(n))
        while unsearched:
            curr = unsearched.pop()
            q = [curr]
            component = set(q)
            while q:
                curr = q.pop()
                for neighbor in G[curr]:
                    if neighbor not in component:
                        q.append(neighbor)
                        component.add(neighbor)
            unsearched -= component
            components.append(component)
        components = [len(component) for component in components]
        #print(components)
        return (sum(components)*sum(components) - sum([c*c for c in components]))//2
