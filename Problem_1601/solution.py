import itertools
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result = 0
        r = len(requests)
        for mask in itertools.product((False,True), repeat=r):
            buildings = [0] * n
            for used,req in zip(mask, requests):
                if used:
                    buildings[req[0]] -= 1
                    buildings[req[1]] += 1
            if not any(buildings):
                result = max(result, sum(mask))
        return result
