import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            while stack and (lcm := math.lcm(i, stack[-1])) != i * stack[-1]:
                stack.pop()
                i = lcm
            stack.append(i)
        return stack
