class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1
        unsearched = set(range(len(edges)))
        while unsearched:
            curr = unsearched.pop()
            component = {curr:0}
            while True:
                curr = edges[curr]
                if curr == -1:
                    break
                if curr in component:
                    result = max(result, len(component) - component[curr])
                    break
                if curr not in unsearched:
                    break
                unsearched.remove(curr)
                component[curr] = len(component)
        return result
