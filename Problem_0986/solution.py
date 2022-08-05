class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i1, i2 = 0, 0
        while i1 < len(firstList) and i2 < len(secondList):
            # if there is currently an overlap
            i_start = max(firstList[i1][0], secondList[i2][0])
            i_end = min(firstList[i1][1], secondList[i2][1])
            #print(i1,i2, firstList[i1], secondList[i2], i_start, i_end)
            if i_start <= i_end:
                result.append((i_start, i_end))
                if firstList[i1][1] == i_end:
                    i1 += 1
                if secondList[i2][1] == i_end:
                    i2 += 1
            else:
                if firstList[i1][0] == min(firstList[i1][0], secondList[i2][0]):
                    i1 += 1
                else:
                    i2 += 1
        return result
