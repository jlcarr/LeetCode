class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        col += 2
        self.disjoint = [-1] * (row*col)
        def find(v):
            while v != self.disjoint[v]:
                self.disjoint[v] = self.disjoint[self.disjoint[v]]
                v = self.disjoint[v]
            return v

        def union(v1, v2):
            # Union by rank optimization
            root1, root2 = find(v1), find(v2)
            if root1 <= root2:
                self.disjoint[root2] = root1
            else:
                self.disjoint[root1] = root2

        # add left and right sides to sets
        left = 0 * col + 0
        self.disjoint[left] = left
        for i in range(row):
            num = i * col + 0
            self.disjoint[num] = num
            union(left, num)
        right = 0 * col + (col-1)
        self.disjoint[right] = right
        for i in range(row):
            num = i * col + (col-1)
            self.disjoint[num] = num
            union(right, num)

        # Run through the days
        for day,new_cell in enumerate(cells):
            #print(self.disjoint)
            new_cell = tuple(new_cell)
            i,j = new_cell
            i -= 1
            num = i * col + j
            if self.disjoint[num] == -1:
                self.disjoint[num] = num
            root = find(num)
            # check for adjacent cells to union
            for ip in [i-1, i, i+1]:
                for jp in [j-1, j, j+1]:
                    if not ((0 <= ip < row) and (0 <= jp < col)):
                        continue
                    if self.disjoint[ip * col + jp] != -1:
                        union(ip * col + jp, root)
            # check for connection
            if find(right) == find(left):
                return day
        #print(self.disjoint)
        return -1
