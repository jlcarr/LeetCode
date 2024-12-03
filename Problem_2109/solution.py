class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = spaces[::-1]
        result = []
        for i,c in enumerate(s):
            if spaces and spaces[-1] == i:
                result.append(' ')
                spaces.pop()
            result.append(c)
        return ''.join(result)
