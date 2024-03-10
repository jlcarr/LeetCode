class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # sort all numbers with indices, find groups, sort those plus indices, and place
        sort = sorted([(n,i) for i,n in enumerate(nums)])
        groups = []
        faction = sort[0][0]
        currgroup = []
        for n,i in sort:
            if n-faction <= limit:
                currgroup.append((n,i))
            else:
                groups.append(currgroup)
                currgroup = [(n,i)]
            faction = n
        if currgroup:
            groups.append(currgroup)
        
        result = [0]*len(nums)
        for group in groups:
            vals = [i[0] for i in group]
            indices = sorted([i[1] for i in group])
            for i,v in zip(indices,vals):
                result[i] = v
        return result
