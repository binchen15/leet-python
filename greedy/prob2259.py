# 10% solution
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        l = []
        for i, c in enumerate(number):
            if c == digit:
                l.append(number[:i] + number[i+1:])

        l.sort(key=int, reverse=True)
        return l[0]

# 30% solution
# find first occurence which is smaller than next digit
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        candies= []
        for i, c in enumerate(number):
            if c == digit:
                candies.append(i)

        li = max(candies)

        for i in candies:
            if i == li or number[i+1] > digit:
                return number[:i] + number[i+1:]
