class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        loop_gas = sum(gas) - sum(cost)
        if loop_gas < 0:
            return -1
        
        curr_val = 0
        min_val = 0
        min_index = 0
        
        n = len(gas)
        for i in range(n):
            #print(i,curr_val)
            if curr_val < min_val:
                min_val = curr_val
                min_index = i
            curr_val += gas[i] - cost[i]
            
        return min_index
