import heapq
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = tuple([(c - 1) % 6 for row in board for c in row])
        index = [i for i,c in enumerate(board) if c == 5][0]
        # A*
        def dist(state):
            return sum(
                abs((i % 3) - (c % 3)) + abs((i // 3) - (c // 3))
                for i,c in enumerate(state)
            )

        costs = {board:0}
        d = dist(board)
        if d == 0:
            return 0
        q = [(d, index//3, index%3, board)]
        while q:
            print(q)
            totcost, i,j, board = heapq.heappop(q)
            currcost = costs[board]
            for ii,jj in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                if not (0 <= ii < 2) or not (0 <= jj < 3):
                    continue
                # swap
                newboard = list(board)
                newboard[3*i + j] = newboard[3*ii + jj]
                newboard[3*ii + jj] = 5
                newboard = tuple(newboard)
                # add
                if newboard not in costs or costs[newboard] > currcost+1:
                    costs[newboard] = currcost+1
                    d = dist(newboard)
                    if d == 0:
                        return currcost + 1
                    heapq.heappush(q, (currcost + 1 + d, ii, jj, newboard))
        return -1

