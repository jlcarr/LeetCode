# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Keep track of strings of 2 values found looking for invalids
        self.runs = []
        self.first_node = None
        self.backup = None
        self.second_node = None
        
        def track_swaps(node):
            #print('order:', node.val)
            # Look for the swapped
            self.runs.append(node)
            if len(self.runs) == 2 and not (self.runs[0].val < self.runs[1].val):
                if not self.first_node:
                    self.first_node = self.runs[0]
                    self.backup = self.runs[1]
                else:
                    self.second_node = self.runs[1]
            if len(self.runs) == 2:
                self.runs.pop(0)
        
        # Morris in-order traversal with a stack
        curr = root
        while curr:
            #print('searching: ',curr.val)
            # if we are at the current smallest position
            if not curr.left:
                track_swaps(curr)
                curr = curr.right
            # otherwise hunt for next
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                    
                # edit the tree so that the right-most leaf now points up to its larger ancestor
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    # Undo the change before by breaking the cycle
                    prev.right = None
                    track_swaps(curr)
                    # onto the next
                    curr = curr.right
        
        if not self.second_node:
            self.second_node = self.backup
            
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
