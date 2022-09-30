# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        result = []
        def ancestor(curr, rem):
            if not curr:
                return
            if rem == 0:
                print('ancestor', curr.val)
                result.append(curr.val)
                return
            ancestor(curr.left, rem-1)
            ancestor(curr.right, rem-1)
            
        def search(curr):
            if not curr:
                return -1
            print('searching', curr.val)
            if curr == target:
                ancestor(curr.left, k-1)
                ancestor(curr.right, k-1)
                return k-1
            
            # left
            s = search(curr.left)
            if s >= 0:
                if s == 0:
                    print('left descendant', curr.val)
                    result.append(curr.val)
                    return -1
                else:
                    ancestor(curr.right, s-1)
                    return s-1
            
            # right
            s = search(curr.right)
            if s >= 0:
                if s == 0:
                    print('right descendant', curr.val)
                    result.append(curr.val)
                    return -1
                else:
                    ancestor(curr.left, s-1)
                    return s-1
            return -1
        
        search(root)
        return result
            
