class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(reverse=True)
        monostack = []
        for price, beauty in items:
            while monostack and monostack[-1][1] < beauty:
                monostack.pop()
            monostack.append((price,beauty))
        monostack = monostack[::-1]

        result = [0] * len(queries)

        queries = sorted([(q,i) for i,q in enumerate(queries)])
        while queries and monostack:
            while monostack and monostack[-1][0] > queries[-1][0]:
                monostack.pop()
            if monostack:
                result[queries[-1][1]] = monostack[-1][1]
            queries.pop()

        return result



