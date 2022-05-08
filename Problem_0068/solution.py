class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_arr = []
        line_len = 0
        while words:
            w = words.pop(0)
            if line_len + len(w) > maxWidth:
                line_len -= len(line_arr)
                spaces = maxWidth - line_len
                if len(line_arr) == 1:
                    line = line_arr[0] + ' ' * (spaces)
                else:
                    all_spaces = spaces // (len(line_arr)-1)
                    left_spaces = spaces % (len(line_arr)-1)
                    line = ''
                    for i in range(len(line_arr)):
                        line += line_arr[i]
                        if i < len(line_arr)-1:
                            line += ' ' * all_spaces
                            if i < left_spaces:
                                line += ' '
                result.append(line)
                line_len = 0
                line_arr = []
            line_arr.append(w)
            line_len += len(w) + 1
        if line_arr:
            line_len -= 1
            result.append(' '.join(line_arr) + ' ' * (maxWidth - line_len))
            
        return result
