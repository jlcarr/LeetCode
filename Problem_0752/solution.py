import heapq
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set([tuple(map(int,i)) for i in deadends])
        self.target = tuple(map(int,target))

        start = (0,0,0,0)
        if start in deadends:
            return -1
        if start == self.target:
            return 0
        costs = {start: 0}
        q = [(self.dist(start), start)]
        #print(q)
        while q:
            est, curr = heapq.heappop(q)
            #print("curr:", curr, est)
            for i in range(4):
                for di in [-1,1]:
                    adj = tuple((v+di*(j==i))%10 for j,v in enumerate(curr))
                    if adj in deadends:
                        continue
                    if adj == self.target:
                        return costs[curr] + 1
                    if adj not in costs:
                        costs[adj] = costs[curr] + 1
                        heapq.heappush(q, (costs[adj]+self.dist(adj), adj))
                        #print("New adj:", adj, costs[adj]+self.dist(adj), costs[adj], self.dist(adj))
        return -1

    def dist(self, v):
        return sum(min((i-j)%10, (j-i)%10) for i,j in zip(self.target, v))
