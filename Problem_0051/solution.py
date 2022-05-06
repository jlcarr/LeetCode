class Solution:
    def formatPerm(self, perm):
        n = len(perm)
        result = []
        for i in range(n):
            row = '.'*perm[i] + 'Q' + '.'*(n-1-perm[i])
            result.append(row)
        return result
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # restrictions:
        #   l: move index left
        #   r: move index right
        #   c: keep index
        def perm_search(depth=0, restrictions=dict()):
            result = []
            
            new_restrictions = dict()
            for i,m in restrictions.items():
                if 'c' in m:
                    if i not in new_restrictions:
                        new_restrictions[i] = ''
                    new_restrictions[i] += 'c'
                if 'l' in m and i > 0:
                    if i-1 not in new_restrictions:
                        new_restrictions[i-1] = ''
                    new_restrictions[i-1] += 'l'
                if 'r' in m  and i < n-1:
                    if i+1 not in new_restrictions:
                        new_restrictions[i+1] = ''
                    new_restrictions[i+1] += 'r'
                    
            if len(new_restrictions) == n:
                return []
                
            for i in range(n):
                if i not in new_restrictions:
                    if depth == n-1:
                        return [[i]]
                    
                    new_restrictions[i] = 'clr'
                    sub_result = perm_search(depth=depth+1, restrictions=new_restrictions)
                    del new_restrictions[i]
                    
                    for res in sub_result:
                        result.append([i] + res)
                        
            return result
        perms = perm_search()
        return [self.formatPerm(p) for p in perms]
