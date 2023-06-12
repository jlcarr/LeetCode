class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        a,b = None,None
        for n in nums:
            if a is None:
                a,b = n,n
            elif n == b + 1:
                b = n
            else:
                if a == b:
                    result.append(str(a))
                else:
                    result.append(f"{a}->{b}")
                a,b = n,n
        if a == b:
            result.append(str(a))
        else:
            result.append(f"{a}->{b}")
        return result
