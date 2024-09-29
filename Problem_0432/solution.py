class DLL:
    def __init__(self, val, keys=None, next=None, prev=None):
        self.val = val
        if not keys:
            self.keys = set()
        self.next = next
        self.prev = prev

    def __hash__(self):
        return self.val
    
    def __eq__(self, other):
        return self.val == other.val


class AllOne:

    def __init__(self):
        self.s2c = dict()
        self.c2s = dict()
        self.head = None
        self.tail = None
        

    def print(self):
        print(self.s2c)
        print(self.c2s)
        print(self.head.val, self.tail.val)
        curr = self.head
        while curr:
            print(curr.val, curr.keys)
            curr = curr.next
        print()

    def inc(self, key: str) -> None:
        if key in self.s2c:
            # update s2c
            count = self.s2c[key]
            self.s2c[key] = count + 1

            # update c2s and DLL
            self.c2s[count].keys.remove(key)
            if count+1 not in self.c2s: # insertion
                self.c2s[count+1] = DLL(count+1)

                self.c2s[count+1].next = self.c2s[count].next
                self.c2s[count+1].prev = self.c2s[count]
                if self.c2s[count].next: # not max
                    self.c2s[count].next.prev = self.c2s[count+1]
                else:
                    self.tail = self.c2s[count+1]
                self.c2s[count].next = self.c2s[count+1]
            self.c2s[count+1].keys.add(key)

            if not self.c2s[count].keys: # removal
                self.c2s[count].next.prev = self.c2s[count].prev
                if self.c2s[count].prev: # not min
                    self.c2s[count].prev.next = self.c2s[count].next
                else:
                    self.head = self.c2s[count].next
                del self.c2s[count]
        else:
            # update s2c
            self.s2c[key] = 1

            # update c2s and DLL
            if 1 not in self.c2s: # insertion
                self.c2s[1] = DLL(1)

                self.c2s[1].next = self.head
                if self.head: # not max
                    self.head.prev = self.c2s[1]
                else:
                    self.tail = self.c2s[1]
                self.head = self.c2s[1]
            self.c2s[1].keys.add(key)
        #print("inc", key)
        #self.print()
        

    def dec(self, key: str) -> None:
        count = self.s2c[key]

        if count > 1:
            # update s2c
            self.s2c[key] = count - 1

            # update c2s and DLL
            self.c2s[count].keys.remove(key)
            if count-1 not in self.c2s: # insertion
                self.c2s[count-1] = DLL(count-1)

                self.c2s[count-1].next = self.c2s[count]
                self.c2s[count-1].prev = self.c2s[count].prev
                if self.c2s[count].prev: # not min
                    self.c2s[count].prev.next = self.c2s[count-1]
                else:
                    self.head = self.c2s[count-1]
                self.c2s[count].prev = self.c2s[count-1]
            self.c2s[count-1].keys.add(key)

            if not self.c2s[count].keys: # removal
                self.c2s[count].prev.next = self.c2s[count].next
                if self.c2s[count].next: # not max
                    self.c2s[count].next.prev = self.c2s[count].prev
                else:
                    self.tail = self.c2s[count].prev
                del self.c2s[count]
        else:
            # update s2c
            del self.s2c[key]
            not self.c2s[1].keys.remove(key)

            if not self.c2s[1].keys: # removal
                if self.c2s[1].next: # not max
                    self.c2s[1].next.prev = None
                else:
                    self.tail = None
                self.head = self.c2s[1].next
                del self.c2s[1]
        #print("dec", key)
        #self.print()
        

    def getMaxKey(self) -> str:
        if not self.tail:
            return ""
        val = self.tail.keys.pop()
        self.tail.keys.add(val)
        #print("getMaxKey")
        #self.print()
        return val


    def getMinKey(self) -> str:
        if not self.head:
            return ""
        val = self.head.keys.pop()
        self.head.keys.add(val)
        #print("getMinKey")
        #self.print()
        return val


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
