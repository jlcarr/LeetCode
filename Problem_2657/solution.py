class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        unmatched = set()
        C = []
        for i,ab in enumerate(zip(A,B)):
            for x in ab:
                if x in unmatched:
                    unmatched.remove(x)
                else:
                    unmatched.add(x)
            C.append(1+i-len(unmatched)//2)
        return C


