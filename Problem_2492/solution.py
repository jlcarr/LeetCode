class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # parse graph
        result = 0
        G = {i+1:dict() for i in range(n)}
        for a,b,distance in roads:
            G[a][b] = distance
            G[b][a] = distance
            result += distance
        
        # BFS
        searched = set()
        q = [1]
        while q:
            curr = q.pop()
            for neighbor, distance in G[curr].items():
                result = min(result, distance)
                if neighbor not in searched:
                    q.append(neighbor)
                    searched.add(neighbor)
        return result
