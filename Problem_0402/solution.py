from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        output = deque()
        for c in num:
            while k > 0 and output and c < output[-1]:
                output.pop()
                k -= 1
            output.append(c)
        while k > 0:
            output.pop()
            k -= 1
        while output and output[0] == '0':
            output.popleft()
        if not output:
            return '0'
        return ''.join(output)
