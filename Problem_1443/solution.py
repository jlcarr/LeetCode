class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        parents = [-1]*n
        for e in edges:
            parents[e[1]] = e[0]

        result = 0
        queue = [i for i,a in enumerate(hasApple) if a and i != 0]
        found = set(queue)
        found.add(0)
        while queue:
            curr = queue.pop()
            result += 2
            parent = parents[curr]
            if parent not in found:
                found.add(parent)
                queue.append(parent)
        return result
