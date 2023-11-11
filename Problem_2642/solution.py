import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.G = {i:dict() for i in range(n)}
        for e in edges:
            self.G[e[0]][e[1]] = e[2]
        

    def addEdge(self, edge: List[int]) -> None:
        self.G[edge[0]][edge[1]] = edge[2]
        

    def shortestPath(self, node1: int, node2: int) -> int:
        costs = {node1: 0}
        q = [(0, node1)]
        while q:
            cost, node = heapq.heappop(q)
            if node == node2:
                return cost
            if cost > costs[node]:
                continue
            for e in self.G[node].items():
                if e[0] in costs and costs[e[0]] <= cost + e[1]:
                    continue
                costs[e[0]] = cost + e[1]
                heapq.heappush(q, (costs[e[0]], e[0]))
        return -1

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
