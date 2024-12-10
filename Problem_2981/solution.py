class Solution:
    def maximumLength(self, s: str) -> int:
        cache = [[None,0,None,0] for _ in range(26)]
        p = s[0]
        ip = 0
        s += '.'
        for i,c in enumerate(s):
            if c != p:
                pord = ord(p) - ord('a')
                if cache[pord][0] is None or cache[pord][0] < i-ip:
                    cache[pord] = [i-ip, 1, cache[pord][0], cache[pord][1]]
                elif cache[pord][0] == i-ip:
                    cache[pord][1] += 1
                elif cache[pord][2] is None or cache[pord][2] < i-ip:
                    cache[pord][2] = i-ip
                    cache[pord][3] = 1
                elif cache[pord][2] == i-ip:
                    cache[pord][3] += 1
                p = c
                ip = i
        #print(cache)
        result = 0
        for max1,cmax1, max2,cmax2 in cache:
            if max1 is None:
                continue
            #print(max1-2)
            result = max(result, max1-2) # auto longest
            if cmax1 >= 3: # appears all 3 sep
                result = max(result, max1)
            if cmax1 >= 2:
                result = max(result, max1-1)
            if max2 is not None and max2 == max1-1:
                result = max(result, max1-1)
        if result == 0:
            return -1
        return result

