class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # find set of greatest leading 1
        # for each find their greatest leading 0
        # find other values that fit
        
        n = len(f"{max(nums):b}")
        nums.sort()
        nums = [f"{i:b}".zfill(n) for i in nums]
        #print(nums)
        
        def find_flip(l,r, pos):
            if nums[l][pos] == nums[r][pos]:
                return -1
            while nums[l][pos] == nums[l+1][pos]:
                m = (l+r)//2
                if nums[m][pos] == '0':
                    l = m
                else:
                    r = m
            return l
        
        # hunt
        result = 0
        for c in nums: # all candidates
            #print('candidate', c)
            l, r = 0, len(nums)-1
            curr = 0
            for pos in range(n): # run over all the bits
                curr *= 2
                m = find_flip(l,r, pos)
                #print(l,r, m)
                if m != -1:
                    if c[pos] == '0':
                        l = m+1
                    else:
                        r = m
                curr += int(c[pos] != nums[l][pos])
            #print('found', l,r, nums[l], curr)
            result = max(result, curr)

        return result
