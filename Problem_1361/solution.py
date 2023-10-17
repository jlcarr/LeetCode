class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find root
        used = set(range(n))
        for l,r in zip(leftChild, rightChild):
            if l in used:
                used.remove(l)
            if r in used:
                used.remove(r)
        
        if len(used) != 1:
            return False
        
        # make sure no cycles and only 1 path to each node
        root = used.pop()
        q = [root]
        found = set(q)
        while q:
            curr = q.pop()
            l = leftChild[curr]
            if l != -1:
                if l in found:
                    return False
                else:
                    found.add(l)
                    q.append(l)
            r = rightChild[curr]
            if r != -1:
                if r in found:
                    return False
                else:
                    found.add(r)
                    q.append(r)
        return len(found) == n
