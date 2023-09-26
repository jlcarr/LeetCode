class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        final_pos = dict()
        for i,c in enumerate(s):
            final_pos[c] = i

        stack = []
        instack = set()
        for i,c in enumerate(s):
            if c not in instack:
                while stack and stack[-1] > c and final_pos[stack[-1]] > i:
                    instack.remove(stack.pop())

                stack.append(c)
                instack.add(c)

        return ''.join(stack)
