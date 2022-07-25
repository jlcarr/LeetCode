class Tree_Node:
    def __init__(self, vals):
        l = len(vals)
        if l == 1:
            self.v = vals[0]
            self.left = None
            self.right = None
        else:
            left, v, right = vals[:l//2], vals[l//2], vals[l//2+1:]
            self.left = Tree_Node(left)
            self.v = v
            self.right = None
            if right:
                self.right = Tree_Node(right)
        self.count = 0
        self.child_count = 0

    def __repr__(self):
        return str(self)

    def __str__(self, depth=0):
        result = "\t"*depth + f"{self.v} ({self.count}, {self.child_count})"
        if self.left is not None:
            result += "\n" + self.left.__str__(depth=depth+1)
        if self.right is not None:
            result += "\n" + self.right.__str__(depth=depth+1)
        return result
        
    def insert(self, v): 
        if v == self.v:
            self.count += 1
            return
        self.child_count += 1
        if v < self.v and self.left:
            self.left.insert(v)
        elif v > self.v and self.right:
            self.right.insert(v) 

    def count_gt(self, v):
        if v > self.v:
            return self.right.count_gt(v) if self.right else 0
        result = 0
        if self.right: result += self.right.count + self.right.child_count
        if v < self.v: result += self.count
        if self.left: result += self.left.count_gt(v)
        return result

    def count_lt(self, v):
        if v < self.v:
            return self.left.count_lt(v) if self.left else 0
        result = 0
        if self.left: result += self.left.count + self.left.child_count
        if v > self.v: result += self.count
        if self.right: result += self.right.count_lt(v)
        return result

    def count_range(self, l, r):
        return self.count + self.child_count - self.count_gt(r) - self.count_lt(l)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Using cumsum technique we get
        # S(i,j) = cumsum[j+1] - cumsum[i]
        # Which means all valid ranges are defined by
        # upper >= cumsum[j+1] - cumsum[i] >= lower
        # which means for a given j we need to count all i such that
        # cumsum[j+1] - upper <= cumsum[i] <= cumsum[j+1] - lower
        if all([n < lower and n <= 0 for n in nums]) or all([n > upper and n >= 0 for n in nums]):
            return 0
        cumsum = [0]
        for j,n in enumerate(nums):
            cumsum.append(cumsum[j] + n)
        
        result = 0
        tree = Tree_Node(sorted(cumsum))
        tree.insert(0)
        #print(tree)
        for j,n in enumerate(nums):
            # update the cumsum
            # get count of previous values falling in range
            l = cumsum[j+1] - upper
            r = cumsum[j+1] - lower
            result += tree.count_range(l,r)
            # update the BBST
            tree.insert(cumsum[j+1])
            #print(f"n {n}, c {cumsum[j+1]}, l {l}, r {r}, res {result}")
            #print(tree)
        return result
