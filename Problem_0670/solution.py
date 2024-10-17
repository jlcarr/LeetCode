class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))[::-1]
        imax = 0
        vmax = num_list[0]
        itake, igive = 0, 0
        for i,c in enumerate(num_list):
            if c < vmax:
                itake = i
                igive = imax
            elif c > vmax:
                imax = i
                vmax = c
        num_list[itake],num_list[igive] = num_list[igive],num_list[itake]
        return int(''.join(num_list[::-1]))
