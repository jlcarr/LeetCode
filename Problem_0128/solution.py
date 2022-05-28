class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start2end = dict()
        end2start = dict()
        nums = set(nums)
        
        for i in nums:
            #print(start2end, end2start)
            #print(i)
            if i in start2end and i in end2start:
                new_start = end2start.pop(i)
                new_end = start2end.pop(i)
                end2start[new_end] = new_start
                start2end[new_start] = new_end
            elif i in start2end:
                end2start[start2end[i]] = i-1
                start2end[i-1] = start2end[i]
                del start2end[i]
            elif i in end2start:
                start2end[end2start[i]] = i+1
                end2start[i+1] = end2start[i]
                del end2start[i]
            else:
                start2end[i-1] = i+1
                end2start[i+1] = i-1
            
        #print(start2end, end2start)
        return max([v-k-1 for k,v in start2end.items()])
