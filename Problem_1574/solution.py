class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # find first adjacent violation and start subarray including right.
        # find last adjacent violation and end subarray including left.
        # go down through the left side and keep a pointer on the right side to match

        first_violation = None
        last_violation = None
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                last_violation = i
                if first_violation is None:
                    first_violation = i+1
        
        if first_violation is None:
            return 0
        #print('violations', first_violation, last_violation)
        result = min(last_violation + 1, len(arr) - first_violation)
        #print('chop result', result)

        #r = last_violation + 1
        r = len(arr) - 1
        for l in range(first_violation - 1, -1, -1):
            while r-1 > last_violation and arr[l] <= arr[r-1]:
                r -= 1
            #print(l, r, arr[l], arr[r], result)
            if arr[l] <= arr[r]:
                result = min(result, r - l - 1)

        return result
