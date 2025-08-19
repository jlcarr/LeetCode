import itertools
import functools
import fractions
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        @functools.cache
        def rec(cards):
            for i1,i2 in itertools.combinations(range(len(cards)), 2):
                rem = [v for k,v in enumerate(cards) if k != i1 and k != i2]
                for i,j,op in [(i1,i2,operator.add), (i1,i2,operator.sub), (i2,i1,operator.sub), (i1,i2,operator.mul), (i1,i2,operator.truediv), (i2,i1,operator.truediv)]:
                    if cards[j] == 0 and op == operator.truediv:
                        continue
                    result = op(cards[i], cards[j])
                    if (not rem and result == 24) or rec(tuple(sorted(rem + [result]))):
                        return True
            return False

        return rec(tuple(map(fractions.Fraction, cards)))
