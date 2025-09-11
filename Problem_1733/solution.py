class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(ls) for ls in languages]
        friends = set([i for u,v in friendships for i in (u,v) if not (languages[u-1] & languages[v-1])])
        result = len(friends)
        for l in range(1, n+1):
            result = min(result, sum(l not in languages[i-1] for i in friends))
        return result

