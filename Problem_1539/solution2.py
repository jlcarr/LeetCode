class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        index = 0
        while True:
            #print(curr, index, k)
            if index < len(arr) and arr[index] == curr:
                index += 1
            else:
                k -= 1
            if k == 0:
                return curr
            curr += 1
        return -1
