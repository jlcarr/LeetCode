class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.i = 0
        self.imax = 0
        

    def visit(self, url: str) -> None:
        self.i += 1
        if len(self.hist) <= self.i:
            self.hist.append(url)
        else:
            self.hist[self.i] = url

        self.imax = self.i
        

    def back(self, steps: int) -> str:
        self.i = max(self.i-steps, 0)
        return self.hist[self.i]
        

    def forward(self, steps: int) -> str:
        self.i = min(self.i+steps, self.imax)
        return self.hist[self.i]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
