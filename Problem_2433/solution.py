class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        prev = 0
        for v in pref:
            arr.append(prev ^ v)
            prev = v
        return arr
        # 5 = 101 = 101 = 5
        # 7 = 111 = 010 = 2
