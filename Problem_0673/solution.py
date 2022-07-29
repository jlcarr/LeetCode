class BST:
    def __init__(self,vals):
        n = len(vals)
        mid = n//2
        v = vals[mid]
        self.v = v
        self.left = None
        self.right = None
        left_vals = vals[:mid]
        if left_vals:
            self.left = BST(left_vals)
        right_vals = vals[mid+1:]
        if right_vals:
            self.right = BST(right_vals)
        
        self.max_l = 0
        self.max_l_count = 0
        self.left_children = False
        self.right_children = False
            
    def __repr__(self, depth=0):
        result = '\t'*depth + f"{self.v} ({self.max_l}x{self.max_l_count}) ({self.left_children},{self.right_children})\n"
        if self.left:
            result += self.left.__repr__(depth=depth+1)
        if self.right:
            result += self.right.__repr__(depth=depth+1)
        return result
    
    def insert(self, v, max_l, max_l_count):
        if v == self.v:
            if max_l > self.max_l:
                self.max_l_count = 0
            self.max_l = max_l
            self.max_l_count += max_l_count
        elif v < self.v and self.left:
            self.left_children = True
            self.left.insert(v, max_l, max_l_count)
        elif v > self.v and self.right:
            self.right_children = True
            self.right.insert(v, max_l, max_l_count)
        
    def count_max_paths(self, v, max_l=1, max_l_count=1):
        if self.left_children: #search through all smaller
            max_l, max_l_count = self.left.count_max_paths(v,max_l,max_l_count)
        if v > self.v:
            if self.max_l+1 > max_l: # if tacking on would result in a new longest
                max_l = self.max_l+1
                max_l_count = 0
            if self.max_l+1 == max_l: # if these are longest add to the count
                max_l_count += self.max_l_count
            if self.right_children: # if there are more to search
                max_l, max_l_count = self.right.count_max_paths(v,max_l,max_l_count)
        return max_l, max_l_count

    def find_max_ls(self,max_l=0, max_l_count=0):
        if self.max_l > max_l:
            max_l = self.max_l
            max_l_count = 0
        if self.max_l == max_l:
            max_l_count += self.max_l_count
            
        if self.left_children:
             max_l, max_l_count = self.left.find_max_ls(max_l=max_l, max_l_count=max_l_count)
        if self.right_children:
            max_l, max_l_count = self.right.find_max_ls(max_l=max_l, max_l_count=max_l_count)
        return max_l, max_l_count
        
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        bst = BST(sorted(list(set(nums))))
        for n in nums:
            max_l, max_l_count = bst.count_max_paths(n)
            bst.insert(n, max_l, max_l_count)
            #print("insert", n)
            #print(bst)
        max_l, max_l_count = bst.find_max_ls()
        return max_l_count
