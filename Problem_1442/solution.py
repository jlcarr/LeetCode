from collections import defaultdict, Counter
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a == b
        # arr[i] ^ ... ^ arr[j-1] == arr[j] ^ ... ^ arr[k]
        # cum[i-1] ^ cum[j-1] == cum[j-1] ^ cum[k]
        # cum[i-1] == cum[k]

        # j == k -> arr[i] ^ ... ^ arr[k-1] == arr[k]
        # j == k -> cum[i-1] ^ cum[k-1] == arr[k]
        # j == k -> cum[i-1] == cum[k]

        counter = Counter()
        cum = defaultdict(int)

        counter[0] = 1
        cum[0] = -1

        result = 0
        acc = 0
        for i,v in enumerate(arr):
            acc ^= v
            result += counter[acc] * (i-1) - cum[acc]
            #print(acc)
            counter[acc] += 1
            cum[acc] += i
        #print(counter)
        return result
        
