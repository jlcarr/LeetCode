class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort not in groups:
                groups[s_sort] = dict()
            if s not in groups[s_sort]:
                groups[s_sort][s] = 0
            groups[s_sort][s] += 1
        
        return [[v for v,count in g.items() for i in range(count)] for g in groups.values()]
            
