class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        curr = None
        for i in intervals:
            if curr:
                if curr[-1] < i[0]:
                    result.append(curr)
                    curr = i
                elif curr[-1] < i[-1]:
                    curr[-1] = i[-1]
            else:
                curr = i
        if curr:
            result.append(curr)
        return result
