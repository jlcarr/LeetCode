from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        neighbors = dict()
        for i,v in enumerate(arr):
            if v not in neighbors:
                neighbors[v] = set()
            neighbors[v].add(i)

        q1 = deque([0])
        depths1 = {0:0}
        q2 = deque([n-1])
        depths2 = {n-1:0}
        while q1 and q2:
            #1
            curr = q1.pop()
            s = neighbors[arr[curr]] | {max(0, curr-1), min(n-1, curr+1)}
            for neighbor in s:
                if neighbor in depths2:
                    return depths1[curr]+depths2[neighbor]+1
                if neighbor not in depths1:
                    q1.appendleft(neighbor)
                    depths1[neighbor] = depths1[curr]+1
            #2
            curr = q2.pop()
            s = neighbors[arr[curr]] | {max(0, curr-1), min(n-1, curr+1)}
            for neighbor in s:
                if neighbor in depths1:
                    return depths2[curr]+depths1[neighbor]+1
                if neighbor not in depths2:
                    q2.appendleft(neighbor)
                    depths2[neighbor] = depths2[curr]+1

        return -1
                
