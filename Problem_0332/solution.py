class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # state = (curr, rem)
        G = dict()
        for i,(head,tail) in enumerate(tickets):
            if head not in G:
                G[head] = []
            G[head].append(tail)
        
        for k in G.keys():
            G[k].sort()
        
        def rec(curr, rem):
            if rem == 0:
                return [curr]
            if curr not in G:
                return None
            dests = G[curr].copy()
            for i in range(len(dests)):
                G[curr] = dests[:i] + dests[i+1:]
                result = rec(dests[i], rem-1)
                if result:
                    return [curr] + result
            G[curr] = dests
            return None

        curr = "JFK"
        return rec(curr, len(tickets))
