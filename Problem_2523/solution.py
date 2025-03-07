class Solution:
    primes = [2,3]
    def closestPrimes(self, left: int, right: int) -> List[int]:
        pmax = self.primes[-1]
        while pmax <= right:
            pmax += 2
            isprime = True
            for p in self.primes:
                if p * p > pmax:
                    break
                if pmax % p == 0:
                    isprime = False
                    break
            if isprime:
                self.primes.append(pmax)
        #print(self.primes[-4:])
        mindist = right
        result = [-1, -1]
        for p1,p2 in zip(self.primes[:-1],self.primes[1:]):
            if left <= p1 and p2 <= right and p2 - p1 < mindist:
                mindist = p2 - p1
                result = [p1, p2]
        return result
