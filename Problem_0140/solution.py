from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # build a trie
        trie = dict()
        for word in wordDict:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr['END'] = dict()

        #import json
        #print(json.dumps(trie, indent=3))

        @cache
        def dfs_main(i):
            result = []
            curr_word = ''
            curr = trie
            while i < len(s):
                #print(i)
                c = s[i]
                i += 1
                curr_word += c
                # dead end
                if c not in curr:
                    return result

                curr = curr[c]
                #found a word
                if 'END' in curr:
                    #print('found', i, curr_word)
                    if i == len(s):
                        return result + [[curr_word]]
                    sub_result = dfs_main(i)
                    for l in sub_result:
                        result.append([curr_word] + l)
            #print('result', result)
            return result
        result = dfs_main(0)
        return [' '.join(r) for r in result]
