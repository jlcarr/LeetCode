class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjmap = dict()
        for pair in adjacentPairs:
            for node in pair:
                if node not in adjmap:
                    adjmap[node] = []
            adjmap[pair[0]].append(pair[1])
            adjmap[pair[1]].append(pair[0])
        start = None
        for node,adjs in adjmap.items():
            if len(adjs) == 1:
                start = node
                break
        result = [start]

        prev,curr = start, adjmap[start][0]
        while True:
            if len(adjmap[curr]) == 1:
                break
            nextv = adjmap[curr][0] if adjmap[curr][0] != prev else adjmap[curr][1]
            prev,curr = curr,nextv
            result.append(prev)

        result.append(curr)

        return result
