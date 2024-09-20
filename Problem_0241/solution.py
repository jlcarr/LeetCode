from functools import cache
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Parse into ops and numbers
        nums = ['']
        ops = []
        for c in expression:
            if c in '+-*':
                ops.append(c)
                nums.append('')
            else:
                nums[-1] += c
        nums = list(map(int,nums))

        # choose an op to split on
        @cache
        def rec(l,r):
            if l == r:
                return set([nums[l]])
            result = list()
            for i in range(l,r):
                ls = rec(l,i)
                rs = rec(i+1,r)
                #print(l,r,i,ls,rs)
                for la in ls:
                    for ra in rs:
                        if ops[i] == '+':
                            result.append(la+ra)
                        if ops[i] == '-':
                            result.append(la-ra)
                        if ops[i] == '*':
                            result.append(la*ra)
            #print(l,r,result)
            return result
        return rec(0,len(ops))
