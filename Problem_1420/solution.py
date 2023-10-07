from collections import Counter
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m:
            return 0

        vals = [[1]*m] # maps [k changes] -> [m curr max] -> count
        #print(f"i_n 0\n\ti_k 1\n\tvals {vals}")
        for i_n in range(1, n):
            #print("i_n", i_n)
            new_vals = []
            new_max_counts_newk = [0]*m
            for i_k in range(1, len(vals)+1): # changes from prev iteration
                #print("\ti_k", i_k)
                new_max_counts_currk = new_max_counts_newk
                new_max_counts_newk = [0]*m
                max_counts = vals[i_k-1]
                less_than_count = 0
                for i_m in range(1, m+1): # possible maxes
                    new_max_counts_currk[i_m-1] = \
                        (new_max_counts_currk[i_m-1] + max_counts[i_m-1]*i_m) % (10**9 + 7)  # <= currk
                    new_max_counts_newk[i_m-1] = \
                        (new_max_counts_newk[i_m-1] + less_than_count) % (10**9 + 7)
                    less_than_count += max_counts[i_m-1]
                new_vals.append(new_max_counts_currk)
                #print('\tnew_max_counts_currk', new_max_counts_currk)
                #print('\tnew_max_counts_newk', new_max_counts_newk)
            if len(new_vals) < k:
                new_vals.append(new_max_counts_newk)
            vals = new_vals
            #print("\tvals", vals)
            #print()
        
        if len(vals) >= k:
            return sum(vals[k-1]) % (10**9 + 7)
        return 0
