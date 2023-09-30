class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        mono_stack = []
        middle = None
        for n in nums[::-1]:
            if middle is not None and n < middle:
                return True
            while mono_stack and mono_stack[-1] < n:
                middle = mono_stack.pop()
            mono_stack.append(n)

        return False
