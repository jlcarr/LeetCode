import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        
        w = len(words)
        l = len(words[0])
        scan_len = len(s) // l - w
        #print(w,l,scan_len)
        
        words = collections.Counter(words)
        
        if l*w > len(s):
            return []
        
        # for each possible mod-offset
        # chop up s into possible words
        # keep a dict of matches 
            #and a count of terms needed
            # as well as a count of overflow
        
        for offset in range(l):
            # initialize count
            rem = w
            track = words.copy()
            pos = offset
            # initialize the chop
            for i in range(w):
                word = s[pos+i*l:pos+l+i*l]
                if word in track:
                    track[word] -= 1
                    if track[word] >= 0:
                        rem -= 1
            # check for a first solution
            if rem == 0:
                result += [pos]
            
            #print("init", track, rem, scan_len)
            for j in range(scan_len):
                old_word = s[pos:pos+l]
                if old_word in track:
                    track[old_word] += 1
                    if track[old_word] > 0:
                        rem += 1
                        
                new_word = s[pos+w*l:pos+l+w*l]
                if new_word in track:
                    track[new_word] -= 1
                    if track[new_word] >= 0:
                        rem -= 1
                        
                pos += l
                # check if we have a solution
                if rem == 0:
                    result += [pos]
                #print("loop", track)
                #print("res", result)
                #print("rem", rem, "pos", pos, old_word, new_word, offset)
        return result
                
