class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        result = 1
        plants = 0
        seats = 0
        for c in corridor:
            if c == 'P':
                plants += 1
            else:
                seats += 1
                if seats % 2 == 1 and seats > 2:
                    result = result * (plants+1) % mod
                plants = 0
        
        if seats % 2 == 1 or seats == 0:
            return 0
        
        return result
        
