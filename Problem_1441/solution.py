class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i_target = 0
        i_n = 1
        while i_target < len(target):
            while target[i_target] > i_n:
                result.append("Push")
                i_n += 1
                result.append("Pop")
            result.append("Push")
            i_n += 1
            i_target += 1
        return result
