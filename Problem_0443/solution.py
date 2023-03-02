class Solution:
    def compress(self, chars: List[str]) -> int:
        wcursor,rcursor = 0,0
        curr_c = None
        count_c = 0
        while rcursor <= len(chars) :
            if curr_c is None:
                curr_c = chars[rcursor]
            elif rcursor == len(chars) or chars[rcursor] != curr_c:
                chars[wcursor] = curr_c
                wcursor += 1
                if count_c > 1:
                    for num_c in str(count_c):
                        chars[wcursor] = num_c
                        wcursor += 1
                count_c = 0
                curr_c = chars[rcursor] if rcursor < len(chars) else None
            count_c += 1
            rcursor += 1
        #print(chars, wcursor, rcursor)
        while len(chars) > wcursor:
            chars.pop()
        #print(chars)
        return len(chars)
