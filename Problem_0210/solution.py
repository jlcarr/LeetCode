class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        incoming_count = {i:0 for i in range(numCourses)}
        G = {i:[] for i in range(numCourses)}
        for e in prerequisites:
            G[e[1]].append(e[0])
            incoming_count[e[0]] += 1
            
        result = [n for n,count in incoming_count.items() if count == 0]
        i_start = 0
        while i_start < len(result):
            start = result[i_start]
            for e in G[start]:
                incoming_count[e] -= 1
                if incoming_count[e] == 0:
                    result.append(e)
                if incoming_count[e] < 0:
                    return []
            i_start += 1
        if len(result) < numCourses:
            return []
        return result
        
