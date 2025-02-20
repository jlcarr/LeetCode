class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sol = [0]*(2*n-1)
        marked = [False]*n
        def backtrack(pos):
            #print("pos", pos, sol, marked)
            if pos == 2*n-1:
                return all(marked)
            if sol[pos] != 0:
                return backtrack(pos+1)
            for i in range(n):
                if i == n-1:
                    if marked[i]:
                        continue
                    marked[i] = True
                    sol[pos] = 1
                    if backtrack(pos+1):
                        return True
                    sol[pos] = 0
                    marked[i] = False
                    continue
                
                if not marked[i] and pos+n-i < 2*n-1 and sol[pos+n-i] == 0:
                    marked[i] = True
                    sol[pos] = n-i
                    sol[pos+n-i] = n-i
                    if backtrack(pos+1):
                        return True
                    sol[pos+n-i] = 0
                    sol[pos] = 0
                    marked[i] = False
            return False
        
        backtrack(0)
        return sol
