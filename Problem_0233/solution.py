class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0

        remainder = n
        digit_place = 1
        result = 0
        while remainder > 0:
            # extract digit
            digit = remainder % 10
            remainder //= 10
            # count all less than the digit for the 1
            result += remainder * digit_place
            if digit == 1:
                # everything lower can be counted down with a leading 1
                result += n % digit_place + 1
            elif digit > 1:
                # the 1 will eventually contribute a complete count
                result += digit_place
            digit_place *= 10

        return result
