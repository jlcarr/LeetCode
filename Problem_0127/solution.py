class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        # search down
        depth_set = set()
        next_depth = set([beginWord])
        done = False
        depth = 0
        while next_depth:
            print(depth, next_depth)
            depth_set = next_depth
            next_depth = set()
            depth += 1
            for word in depth_set:
                temp = list(word)
                for i,c in enumerate(word):
                    for alpha in range(26):
                        new_c = chr(ord('a')+alpha)
                        temp[i] = new_c
                        temp2 = ''.join(temp)
                        if temp2 == endWord:
                            return depth+1
                        if temp2 in wordList:
                            next_depth.add(temp2)
                            wordList.remove(temp2)
                    temp[i] = c
        return 0
