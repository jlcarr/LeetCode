class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r = 0, 1+(position[-1]-position[0])//(m-1)
        c = 0
        while l < r:
            v = (r+1+l)//2
            # assign
            prev = position[0]
            count = 1
            for p in position[1:]:
                if p-prev >= v:
                    count += 1
                    prev = p
            #print(l,r, v, count)
            if count >= m:
                if l == v:
                    return v
                l = v
            else:
                r = v-1
        return l
