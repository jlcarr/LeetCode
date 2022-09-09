class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = [-1, -1]
        most_recent = [-1,-1]
        curr = 0
        result = 0
        for i,f in enumerate(fruits):
            if f in types:
                most_recent[types.index(f)] = i
                curr += 1
            else:
                if most_recent[0] <= most_recent[1]:
                    curr = i - most_recent[0]
                    most_recent[0] = i
                    types[0] = f
                else:
                    curr = i - most_recent[1]
                    most_recent[1] = i
                    types[1] = f
            result = max(result, curr)
                    
            #print(f, result, types, most_recent)
        return result
