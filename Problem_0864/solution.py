from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        orda, ordz = ord('a'), ord('z')
        orduA, orduZ = ord('A'), ord('Z')
        keys = sorted([cell for row in grid for cell in row if orda <= ord(cell) <= ordz])
        start = [(i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == '@'][0]
        result = -1
        q = deque([(start, (0,)*len(keys), 0)])
        searched = set([(start, (0,)*len(keys))])           
        while q:
            (ipos,jpos), keys, cost = q.pop()
            cost += 1
            for idiff,jdiff in [(ipos-1, jpos), (ipos+1, jpos), 
                (ipos, jpos-1), (ipos, jpos+1)]:
                if not ((0 <= idiff < m) and (0 <= jdiff < n)) \
                    or (grid[idiff][jdiff] == '#'): # bounds and walls
                    continue
                cell = grid[idiff][jdiff]
                # new keys
                new_keys = list(keys)
                ordg = ord(grid[idiff][jdiff])
                if orda <= ordg <= ordz:
                    new_keys[ordg-orda] = 1
                new_keys = tuple(new_keys)
                if all(new_keys): #done
                    return cost
                # already searched
                if ((idiff, jdiff), new_keys) in searched:
                    continue
                # locks
                if (orduA <= ordg <= orduZ) and not new_keys[ord(cell.lower())-orda]:
                    continue

                searched.add(((idiff, jdiff), new_keys))
                q.appendleft(((idiff, jdiff), new_keys, cost))
        return -1
