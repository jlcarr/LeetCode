from functools import cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # This is the number of Hamiltonian paths (not cycles)
        m,n = len(grid), len(grid[0])

        @cache
        def rec(pos, state):
            state = [list(row) for row in state]
            result = 0
            for ip,jp in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_pos = (pos[0]+ip, pos[1]+jp)
                if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and state[new_pos[0]][new_pos[1]] != -1:
                    if state[new_pos[0]][new_pos[1]] == 2 and all([c != 0 for row in state for c in row]):
                        result += 1
                    elif state[new_pos[0]][new_pos[1]] == 0:
                        state[new_pos[0]][new_pos[1]] = -1
                        result += rec(new_pos, tuple(map(tuple,state)))
                        state[new_pos[0]][new_pos[1]] = 0
            state[pos[0]][pos[1]] = 1
            #for row in state:
            #    print(row)
            #print(pos,result)
            return result

        pos = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos = (i,j)
                    grid[i][j] = -1
                if pos is not None:
                    break
            if pos is not None:
                break

        return rec(pos, tuple(map(tuple,grid)))

