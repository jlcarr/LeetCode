class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        div_result = (target // s) * len(nums)
        target = target % s
        if target == 0:
            return div_result
        #print("div_result", div_result, "sum", s)
            
        result = None
        cumsum_map = dict()
        acc = 0
        i = 0
        for _ in range(2):
            for v in nums:
                acc += v
                # check is there
                if acc - target in cumsum_map:
                    range_i = i - cumsum_map[acc - target]
                    if result is None:
                        result = range_i
                    result = min(result, range_i)

                if acc not in cumsum_map:
                    cumsum_map[acc] = i
                cumsum_map[acc] = max(cumsum_map[acc], i)

                i += 1
        if result is None:
            return -1
        return result + div_result
