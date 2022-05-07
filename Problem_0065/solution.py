import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return bool(re.match(r'^[\-\+]?(?:\d+\.?\d*|\d*\.?\d+)(?:[eE][\-\+]?\d+)?$', s))
