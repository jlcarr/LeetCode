class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        G = dict()
        for start,end in prerequisites:
            if start not in G:
                G[start] = set()
            G[start].add(end)
            
        to_search = set(G.keys())
        free = set()
        visited = set()
        def dfs(node):
            print(node)
            if node in to_search:
                to_search.remove(node)
            if node not in G or node in free:
                return True
            visited.add(node)
            for e in G[node]:
                if e in visited:
                    return False
                if not dfs(e):
                    return False
            visited.remove(node)
            free.add(node)
            return True
        
        while to_search:
            v = to_search.pop()
            if not dfs(v):
                return False
            
        return True
