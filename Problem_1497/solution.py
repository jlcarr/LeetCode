from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter([i % k for i in arr])
        for key,count in counts.items():
            if key == 0 or 2*key == k:
                if count % 2 == 1:
                    #print(key, count)
                    return False
            elif counts[k-key] != count:
                #print(key, count)
                return False
        return True
