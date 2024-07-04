class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        kk_lens = [[0 for j in range(k)] for i in range(k)]
        for n in nums:
            # add to rows
            for i in range(k):
                if i == n%k:
                    continue
                if kk_lens[n%k][i] % 2 == 0:
                    kk_lens[n%k][i] += 1
            # add to cols
            for i in range(k):
                if i == n%k:
                    continue
                if kk_lens[i][n%k] % 2 == 1:
                    kk_lens[i][n%k] += 1
            # doubleup
            kk_lens[n%k][n%k] += 1
        return max([max(row) for row in kk_lens])
