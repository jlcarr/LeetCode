class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inv = [[] for _ in graph]
        for i,adj in enumerate(graph):
            for j in adj:
                inv[j].append(i)

        graph = [set(i) for i in graph]

        searchable = [i for i,adj in enumerate(graph) if not adj]
        result = set(searchable)

        while searchable:
            i = searchable.pop()
            for j in inv[i]:
                graph[j].remove(i)
                if not graph[j]:
                    searchable.append(j)
                    result.add(j)
        
        return sorted(list(result))

