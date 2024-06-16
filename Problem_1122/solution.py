class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = len(arr2)
        arr2 = {v:i for i,v in enumerate(arr2)}
        return sorted(arr1, key=lambda k: arr2.get(k, l+k))
