# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = dict()
        parented_nodes = set()
        for parent, child, isLeft in descriptions:
            parented_nodes.add(child)
            if parent not in node_map:
                node_map[parent] = TreeNode(val=parent)
            if child not in node_map:
                node_map[child] = TreeNode(val=child)
            if isLeft == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
        return node_map[(set(node_map.keys()) - parented_nodes).pop()]
