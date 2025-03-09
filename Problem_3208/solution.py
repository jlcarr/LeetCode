class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = len(colors)
        red_even, red_odd = 0, 0
        blue_even, blue_odd = 0, 0
        result = 0
        for i in range(l+k-1):
            if colors[i % l]:
                if i % 2:
                    red_odd += 1
                else:
                    red_even += 1
            else:
                if i % 2:
                    blue_odd += 1
                else:
                    blue_even += 1
            if i >= k:
                if colors[(i-k) % l]:
                    if (i-k) % 2:
                        red_odd -= 1
                    else:
                        red_even -= 1
                else:
                    if (i-k) % 2:
                        blue_odd -= 1
                    else:
                        blue_even -= 1
            result += (red_odd + blue_even == k) or (blue_odd + red_even == k)
            #print(i, result, '', red_even, blue_odd, '',red_odd, blue_even)
        return result
