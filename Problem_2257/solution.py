class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[1]*n for i in range(m)]

        # filter along rows
        guards.sort()
        walls.sort()
        iguard = 0
        iwall = 0
        for i in range(m):
            last_guard = -2
            last_wall = -1
            for j in range(n+1):
                # bring up guard and wall cols
                while iguard < len(guards)-1 and guards[iguard] < [i,j]:
                    iguard += 1
                if guards[iguard] == [i,j]:
                    last_guard = j
                    continue
                while iwall < len(walls)-1 and walls[iwall] < [i,j]:
                    iwall += 1
                if walls[iwall] == [i,j] or j == n:
                    if j < n:
                        cells[i][j] = 0
                    if last_wall < last_guard:
                        for jj in range(last_wall+1,j):
                            cells[i][jj] = 0
                    last_wall = j   

        # filter along columns
        guards = [[g[1],g[0]] for g in guards]
        guards.sort()
        walls = [[w[1],w[0]] for w in walls]
        walls.sort()
        iguard = 0
        iwall = 0
        for j in range(n):
            last_guard = -2
            last_wall = -1
            for i in range(m+1):
                # bring up guard and wall cols
                while iguard < len(guards)-1 and guards[iguard] < [j,i]:
                    iguard += 1
                if guards[iguard] == [j,i]:
                    last_guard = i
                    continue
                while iwall < len(walls)-1 and walls[iwall] < [j,i]:
                    iwall += 1
                if walls[iwall] == [j,i] or i == m:
                    if i < m:
                        cells[i][j] = 0
                    if last_wall < last_guard:
                        for ii in range(last_wall+1,i):
                            cells[ii][j] = 0
                    last_wall = i
        return sum([sum(row) for row in cells])
