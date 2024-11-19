from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #initialize window
        counts = Counter()
        for i in range(k):
            counts[nums[i]] += 1
        maxcount = 0
        subarraysum = 0
        invCounts = [0 for _ in range(k+1)]
        for v,count in counts.items():
            invCounts[count] += 1
            maxcount = max(maxcount, count)
            subarraysum += v * count

        result = 0
        if maxcount == 1:
            result = max(result, subarraysum)
        #print(counts, invCounts)
        # move window
        for i in range(k,len(nums)):
            v_prev = nums[i-k]
            v_new = nums[i]
            if v_prev == v_new:
                continue
            # update counts
            v_prev_count = counts[v_prev]
            v_new_count = counts[v_new]
            #print(i, ':', v_prev, v_prev_count, '-', v_new, v_new_count)
            #print(counts, invCounts)
            #print(subarraysum, maxcount, result)
            counts[v_prev] -= 1
            counts[v_new] += 1
            # update invCounts
            invCounts[v_prev_count] -= 1
            if v_prev_count-1 > 0:
                invCounts[v_prev_count-1] += 1
            if v_new_count > 0:
                invCounts[v_new_count] -= 1
            invCounts[v_new_count+1] += 1
            # update subarraysum and maxcount
            subarraysum += v_new - v_prev
            maxcount = max(maxcount, v_new_count+1)
            if v_prev_count == maxcount and invCounts[v_prev_count] == 0:
                maxcount -= 1
            # update result
            if maxcount == 1:
                result = max(result, subarraysum)
            #print(subarraysum, maxcount, result)
            #print(counts, invCounts)
        
        return result
    
