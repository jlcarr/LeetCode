# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        self.result = ""
        self.index = -1
        
        def dfs(node, parent_index,RL):
            self.result += f"{node.val}|{parent_index}|{RL},"
            self.index += 1
            curr_index = self.index
            if node.left:
                dfs(node.left, curr_index,'L')
            if node.right:
                dfs(node.right, curr_index,'R')
                
        dfs(root, '', '')
        return self.result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_list = []
        data = data.split(',')
        for node in data[:-1]:
            print(node)
            val,index,RL = node.split('|')
            node = TreeNode(int(val))
            node_list.append(node)
            if RL == 'L':
                node_list[int(index)].left = node
            elif RL == 'R':
                node_list[int(index)].right = node
                
        return node_list[0]
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
