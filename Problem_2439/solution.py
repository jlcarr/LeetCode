class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        fin = nums[0]
        acc = 0
        tot = fin

        #print(tot, fin)
        for i in range(1,n):
            tot += nums[i]
            acc = tot - fin
            if acc > fin * i:
                fin = tot // (i+1)
                acc = tot - fin
                if acc > fin*i:
                    fin += 1
            acc = tot - fin
            #print(tot, fin)
        return fin
