# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = re.findall(r"(\-*)(\d+)", traversal)[::-1]
        stack = [(len(D),int(v)) for D,v in stack]
        #print(stack)
        def rec(curr, depth, stack):
            if stack and stack[-1][0] > depth:
                curr.left = TreeNode(val=stack[-1][1])
                stack.pop()
                rec(curr.left, depth+1, stack)
            if stack and stack[-1][0] > depth:
                curr.right = TreeNode(val=stack[-1][1])
                stack.pop()
                rec(curr.right, depth+1, stack)
            return curr

        curr = TreeNode(val=stack[-1][1])
        stack.pop()
        return rec(curr, 0, stack)


