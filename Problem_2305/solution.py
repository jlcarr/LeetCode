class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.result = sum(cookies)
        def search(state, c):
            if c == len(cookies):
                self.result = min(self.result, max(state))
                return
            new_state = list(state)
            for child in range(k):
                new_state[child] += cookies[c]
                if self.result > new_state[child]:
                    search(tuple(new_state), c+1)
                new_state[child] -= cookies[c]
        search((0,) * k, 0)
        return self.result

