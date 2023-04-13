class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for p in popped:
            while not stack or stack[-1] != p:
                if i >= len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1
            stack.pop()
        return True
