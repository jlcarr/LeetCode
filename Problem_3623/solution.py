class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # get list of points on same y
        # pairs same y are seg-lens
        # segs diff y or traps
        mod = 10**9 + 7
        points.sort(key=lambda p:p[1])
        points.append((0, points[-1][1]+1))

        result = 0

        curr_y = points[0][1]
        curr_point_count = 0
        prev_edge_count = 0

        for x,y in points:
            if y == curr_y:
                curr_point_count += 1
            else:
                curr_edges_count = curr_point_count * (curr_point_count-1) //2
                result = (result + prev_edge_count * curr_edges_count) % mod
                #print(y, curr_y, curr_edges_count, prev_edge_count, result)
                prev_edge_count += curr_edges_count
                curr_y = y
                curr_point_count = 1
                

        return result
            
