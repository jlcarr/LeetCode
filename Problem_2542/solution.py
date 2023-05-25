import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)
        curr_sum = 0
        curr_nums1 = []
        result = 0
        for num2,num1 in nums:
            heapq.heappush(curr_nums1, num1)
            curr_sum += num1
            if len(curr_nums1) < k:
                continue
            while len(curr_nums1) > k:
                curr_sum -= heapq.heappop(curr_nums1)
            result = max(result, curr_sum*num2)
        return result
