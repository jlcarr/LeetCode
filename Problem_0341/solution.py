# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [nestedList]
        self.istack = [0]
    
    def _increment(self):
        self.istack[-1] += 1
        while self.stack and self.istack[-1] >= len(self.stack[-1]):
            self.stack.pop()
            self.istack.pop()
            if self.stack:
                self.istack[-1] += 1

    def _queueup(self):
        while self.stack and not self.stack[-1][self.istack[-1]].isInteger():
            l = self.stack[-1][self.istack[-1]].getList()
            if 0 == len(l):
                self._increment()
            else:
                self.stack.append(l)
                self.istack.append(0)

    def next(self) -> int:
        self._queueup()
        result = self.stack[-1][self.istack[-1]].getInteger()
        self._increment()
        return result
        
    def hasNext(self) -> bool:
        self._queueup()
        return bool(self.stack)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
