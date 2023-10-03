class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        result = [-1] * n
        
        # find the SCC cycle sets, and the non-cycles distance to the cycle
        
        searched = set()
        for i in range(n):
            if result[i] != -1:
                continue
            
            # search for cycle
            curr = i
            stack = [curr]
            curr_search = set(stack)
            while edges[curr] not in curr_search and edges[curr] not in searched:
                curr = edges[curr]
                stack.append(curr)
                curr_search.add(curr)
                
            cycle_len = 0
            if edges[curr] not in searched:
                # pull out values onto the stack
                cycle_set = set()
                while stack[-1] != edges[curr]:
                    cycle_set.add(stack.pop())
                    cycle_len += 1
                cycle_set.add(stack.pop())
                cycle_len += 1
                # fill cycle members
                for node in cycle_set:
                    result[node] = cycle_len
            else:
                cycle_len = result[edges[curr]]

            # the rest are distances to stack
            dist_to_cycle = 0
            while stack:
                dist_to_cycle += 1
                result[stack.pop()] = dist_to_cycle + cycle_len
            
            # dont search again
            searched |= curr_search
            
        return result
            
            
                
