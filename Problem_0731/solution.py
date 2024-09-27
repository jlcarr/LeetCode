class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []
        

    def book(self, start: int, end: int) -> bool:
        for s,e in self.double_bookings:
            if end > s and start < e:
                return False
        for s,e in self.bookings:
            if end > s and start < e:
                self.double_bookings.append((max(s,start), min(e,end)))
        self.bookings.append((start,end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
