class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # 1. compute prime scores
        # 2. run through with deque of (prime score, value),
        # to get widest range for each element with curr as max
        # back and forth
        # [19,12,14,6,10,18]
        # [1,2,2,2,2,2] prime score

        # [8,3,9,3,8]
        # [1,1,1,1,1]
        mod = 10**9 + 7

        # primes
        primes = [2,3]
        i = primes[-1]+2
        pmax = max(nums)
        while i*i <= pmax:
            isprime = True
            for p in primes:
                if p*p >= i:
                    break
                if i % p == 0:
                    isprime = False
                    break
            if isprime:
                primes.append(i)
            i += 2
        #print(primes)

        # prime scores
        prime_scores = []
        for x in nums:
            pscore = 0
            for p in primes:
                if x % p == 0:
                    pscore += 1
                while x % p == 0:
                    x //= p
                if x == 1:
                    break
            if x != 1:
                pscore += 1
            prime_scores.append(pscore)
        #print(prime_scores)

        # [3,2,1]
        # left
        q = [] # monotonic stack
        ls = []
        for i,x in enumerate(nums):
            while q and q[-1][0] < prime_scores[i]: # le for min index
                q.pop()
            if q:
                ls.append(q[-1][1]+1)
            else:
                ls.append(0)
            q.append((prime_scores[i], i, x))

        # right
        q = [] # monotonic stack
        rs = []
        for i,x in reversed(list(enumerate(nums))):
            while q and q[-1][0] <= prime_scores[i]: #leq for min index
                q.pop()
            if q:
                rs.append(q[-1][1]-1)
            else:
                rs.append(len(nums)-1)
            q.append((prime_scores[i], i, x))
        rs = rs[::-1]
        #print(ls,rs)

        q = sorted([(x,i) for i,x in enumerate(nums)])
        score = 1
        while k:
            x,i = q.pop()
            rem = min((i+1-ls[i])*(rs[i]+1-i), k)
            score *= pow(x, rem, mod)
            score %= mod
            k -= rem

        return score

