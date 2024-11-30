from collections import Counter, deque
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # this is an eulerian path
        # Hierholzer's algorithm with a deque

        # build graph
        G = dict()
        starts = Counter()
        ends = Counter()
        edges = set()
        for start,end in pairs:
            starts[start] += 1
            ends[end] += 1
            if start not in G:
                G[start] = set()
            G[start].add(end)
            edges.add((start,end))
        #print(G)
        #print(edges)
        # find starts
        totstart = starts - ends
        if totstart:
            totstart = next(iter(totstart.keys()))
        else:
            totstart = None
        # find ends
        totend = ends - starts
        if totend:
            totend = next(iter(totend.keys()))
        else:
            totend = None
        #print(totstart, totend)
        #begin search
        q = deque()
        if totstart is not None:
            q.append(totstart)
        else:
            q.append(pairs[0][0])
        while edges:
            q.appendleft(q.pop())
            while q[-1] in G:
                v = G[q[-1]].pop()
                if not G[q[-1]]:
                    del G[q[-1]]
                edges.remove((q[-1],v))
                #print((q[-1],v), v)
                q.append(v)
                #print(q)
        while (totstart is not None and q[0] != totstart) or (totend is not None and q[-1] != totend):
            q.appendleft(q.pop())
        for i in range(len(q)-1):
            if q[i] == q[i+1]:
                for _ in range(i+1):
                    q.append(q.popleft())
                break
        #print(q)
        q = list(q)
        return list(map(list,zip(q[:-1],q[1:])))
