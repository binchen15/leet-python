#GFG

class Solution:
    def isGoodorBad(self, S):
        # code here

        n = len(S)
        dp_c = [0] * n
        dp_v = [0] * n

        if S[0] =="?":  # wild card
            dp_c[0] = 1
            dp_v[0] = 1
        elif S[0] in "aeiou":
            dp_c[0] = 0
            dp_v[0] = 1
        else:
            dp_c[0] = 1
            dp_v[0] = 0

        for i in range(1, n):
            if S[i] == "?":
                dp_c[i] = 1 + dp_c[i-1]
                dp_v[i] = 1 + dp_v[i-1]
            elif S[i] in "aeiou":
                dp_v[i] = 1 + dp_v[i-1]
            else:
                dp_c[i] = 1 + dp_c[i-1]

            if dp_v[i] > 5 or dp_c[i] > 3:
                return 0

        return 1
