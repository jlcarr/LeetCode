from collections import deque 

def gen_subwords(w):
    return [w[:i] + w[i+1:] for i in range(len(w))]

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        l = len(beginWord)
        alphabet = [chr(ord('a') + i) for i in range(26)]
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        neighbors = [dict() for i in range(l)]
        for w in set([beginWord])|wordList:
            subwords = gen_subwords(w)
            for i, sub_word in enumerate(subwords):
                if sub_word not in neighbors[i]:
                    neighbors[i][sub_word] = []
                neighbors[i][sub_word].append(w)
        
        # find optimal distances
        opt_dist = {beginWord: 1}
        q = deque([beginWord])
        while q:
            curr = q.pop()
            dist = opt_dist[curr]
            if endWord in opt_dist and dist >= opt_dist[endWord]:
                break
            subwords = gen_subwords(curr)
            for i, sub_word in enumerate(subwords):
                for neighbor in neighbors[i][sub_word]:
                    if neighbor in wordList and neighbor not in opt_dist:
                        opt_dist[neighbor] = dist+1
                        q.appendleft(neighbor)
        if endWord not in opt_dist:
            return []
              
        # find optimal paths back
        q = deque([endWord])
        opt_paths = {endWord: [[endWord]]}
        while q:
            curr = q.pop()
            paths = opt_paths[curr]
            dist = opt_dist[curr]
            subwords = gen_subwords(curr)
            for i, sub_word in enumerate(subwords):
                for neighbor in neighbors[i][sub_word]:
                    if neighbor in opt_dist and opt_dist[neighbor] <= dist-1:
                        if neighbor not in opt_paths:
                            opt_paths[neighbor] = []
                            q.appendleft(neighbor)
                        new_paths = [[neighbor]+path for path in paths]
                        opt_paths[neighbor] += new_paths
        #print(opt_paths)
        return opt_paths[beginWord]
