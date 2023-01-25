class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        found1 = {-1: len(edges)+1}
        found2 = {-1: len(edges)+1}
        d = 0
        while node1 not in found1:
            found1[node1] = d
            node1 = edges[node1]
            d += 1
        d = 0
        while node2 not in found2:
            found2[node2] = d
            node2 = edges[node2]
            d += 1

        keys = found1.keys() & found2.keys()
        if not keys:
            return -1

        #print(found1, found2)
        return min(keys, key=lambda k: (max(found1[k], found2[k]),k))
