from functools import cache
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        maxheight = sum(b[1] for b in books)
        @cache
        def dp(i=0, curr_height=books[0][1], curr_width=0):
            while i < len(books) and books[i][1] <= curr_height and curr_width+books[i][0] <= shelfWidth:
                curr_width += books[i][0]
                i += 1
            if i == len(books):
                return curr_height
            result = maxheight
            if curr_width+books[i][0] <= shelfWidth:
                keep_height = dp(i+1, books[i][1], curr_width+books[i][0])
                result = min(result, keep_height)
            # new shelf
            new_shelf_height = curr_height + dp(i+1, books[i][1], books[i][0])
            result = min(result, new_shelf_height)
            return result
        return dp()
