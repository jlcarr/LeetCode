import bisect
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # For each find min p such that nums[i+1] > nums[i] - p
        # i.e. p > nums[i+1] - nums[i]

        # gen p array
        # find max needed
        maxp = max(nums) + 1
        primes = [2]
        i = 3
        while primes[-1] <= maxp:
            isprime = True
            for p in primes:
                if i % p == 0:
                    isprime = False
                    break
                if p*p >= i:
                    break
            if isprime:
                primes.append(i)
            i += 2

        # can't increase any numbers, so start with the back, and ensure correctness
        prev = nums[-1] + 1
        for v in nums[::-1]:
            #print(v, prev)
            if v >= prev:
                i = bisect.bisect_right(primes, v - prev)
                #print(i, primes, v-prev, v, prev)
                p = primes[i]
                if p >= v:
                    return False
                prev = v - p
            else:
                prev = v
        return True
