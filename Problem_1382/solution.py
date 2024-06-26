# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # remove values
        self.vals = []
        def rec_vals(curr):
            if not curr:
                return
            rec_vals(curr.left)
            self.vals.append(curr)
            rec_vals(curr.right)
            curr.left = None
            curr.right = None
        rec_vals(root)
        # build tree
        def rec_build(l,r):
            #print(l,r)
            m = (l+r)//2
            curr = self.vals[m]
            if l < m:
                curr.left = rec_build(l,m-1)
            if r > m:
                curr.right = rec_build(m+1,r)
            return curr
        return rec_build(0,len(self.vals)-1)
