class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort intervals by start
        # run through, keep track of current intervals and next interval end
        # upon end of interval look at last 2 picked to see if need more picks
        # this puts picks as late as possible while satisfying reqs
        intervals.sort(key=lambda x: x[-1])
        last, prev = None, None
        result = 0
        for start,end in intervals:
            if last is None or last < start:
                last, prev = end, end-1
                result += 2
            elif prev < start:
                if last == end:
                    last, prev = end, end-1
                    result += 1
                else:
                    last, prev = end, last
                    result += 1
        # [[1,3],[3,7],[5,7],[7,8]]
        # [2,3,7,]
        return result
