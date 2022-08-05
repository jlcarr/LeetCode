import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0], 0, 0)]
        found = set()
        result = []
        for i in range(k):
            S, i1, i2 = heapq.heappop(heap)
            result.append((nums1[i1], nums2[i2]))
            if i1 < len(nums1)-1 and (i1+1, i2) not in found:
                heapq.heappush(heap, (nums1[i1+1]+nums2[i2], i1+1, i2))
                found.add((i1+1, i2))
            if i2 < len(nums2)-1 and (i1, i2+1) not in found:
                heapq.heappush(heap, (nums1[i1]+nums2[i2+1], i1, i2+1))
                found.add((i1, i2+1))
            if not heap:
                break
        
        return result
