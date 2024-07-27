class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        alphabet = set(source) | set(target) | set(original) | set(changed)
        dist = {i:{j: None if i != j else 0 for j in alphabet} for i in alphabet}
        for s,t,c in zip(original,changed,cost):
            if dist[s][t] is None:
                dist[s][t] = c
            else:
                dist[s][t] = min(dist[s][t], c)
        
        for k in alphabet:
            for i in alphabet:
                for j in alphabet:
                    if dist[i][k] is not None \
                        and dist[k][j] is not None \
                        and (dist[i][j] is None \
                        or dist[i][j] > dist[i][k] + dist[k][j]):
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        result = 0
        for s,t in zip(source,target):
            if s != t:
                if dist[s][t] is None:
                    return -1
                result += dist[s][t]
        return result
