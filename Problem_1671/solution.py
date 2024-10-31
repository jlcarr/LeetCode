class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lr_nums, rl_nums = nums, nums[::-1]
        lr_maxlens, rl_maxlens = [], []
        for nums,maxlens in [(lr_nums,lr_maxlens),(rl_nums,rl_maxlens)]:
            #print('begin traversal')
            maxval_stack = []
            maxlen_stack = []
            for val in nums:
                new_maxval_stack = []
                new_maxlen_stack = []
                new_maxlen = 1
                surpassed = False
                for maxval,maxlen in zip(maxval_stack,maxlen_stack):
                    if maxval < val:
                        new_maxlen = max(new_maxlen, maxlen+1)
                        new_maxval_stack.append(maxval)
                        new_maxlen_stack.append(maxlen)
                    elif maxval == val:
                        new_maxlen = max(new_maxlen, maxlen)
                        new_maxval_stack.append(maxval)
                        new_maxlen_stack.append(new_maxlen)
                        surpassed = True
                    elif maxval > val:
                        if not surpassed:
                            new_maxval_stack.append(val)
                            new_maxlen_stack.append(new_maxlen)
                            surpassed = True
                        if maxlen > new_maxlen:
                            new_maxval_stack.append(maxval)
                            new_maxlen_stack.append(maxlen)
                if not surpassed:
                    new_maxval_stack.append(val)
                    new_maxlen_stack.append(new_maxlen)
                #print(list(zip(new_maxval_stack,new_maxlen_stack)))
                maxval_stack = new_maxval_stack
                maxlen_stack = new_maxlen_stack
                maxlens.append(max(maxlen_stack))
        #print(list(zip(lr_maxlens,rl_maxlens[::-1])))
        return len(lr_nums) - max([i+j-1 for i,j in zip(lr_maxlens,rl_maxlens[::-1]) if i > 1 and j > 1])
