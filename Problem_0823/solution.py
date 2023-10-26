class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulus = 10**9 + 7
        l = len(arr)

        arr.sort()

        indices = {v:i for i,v in enumerate(arr)}
        counts = [1] * len(arr)
        #print(indices)
        
        for i in range(l):
            for j in range(i+1):
                product = arr[i] * arr[j]
                #print(i,j,arr[i], arr[j], product)
                if product <= arr[-1] and product in indices:
                    p = indices[product]
                    #print(i,j,p)
                    symfactor = 1 if i == j else 2
                    counts[p] = (counts[p] + symfactor*counts[i]*counts[j]) % modulus
        #print(counts)
        return sum(counts) % modulus
