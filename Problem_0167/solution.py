class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i,x in enumerate(numbers):
            v = target - x
            l,r = 0, n-1
            while l+1<r:
                m = (l + r)//2
                if numbers[m] <= v:
                    l = m
                else:
                    r = m
            #print(l,r)
            if numbers[l] + x == target and l != i:
                return [i+1,l+1]
            if numbers[r] + x == target and r != i:
                return [i+1,r+1]
