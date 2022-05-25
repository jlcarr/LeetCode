"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        def dfs(curr):
            for e in curr.neighbors:
                if e.val not in val_dict:
                    val_dict[e.val] = Node(e.val)
                    dfs(e)
                val_dict[curr.val].neighbors.append(val_dict[e.val])
             
        sol = Node(val = node.val)
        val_dict = dict()
        val_dict[node.val] = sol
        dfs(node)
        return sol
        
