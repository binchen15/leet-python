# recursion

class Solution:

    @lru_cache(maxsize=None)
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        if "." not in p and "*" not in p:
            return s == p

        if not s:
            return self.helper(p)

        if s[0] == p[0]:
            if p[1] == "*":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            if p[0] == ".":
                if len(p) > 1:
                    if p[1] == "*":
                        return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                    else:
                        return self.isMatch(s[1:], p[1:])
                else:
                    return self.isMatch(s[1:], "")

            elif p[0] in string.ascii_lowercase and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False

    def helper(self, p):
        """test if p match empty string"""
        if not p:
            return True

        if len(p) % 2 != 0:
            return False

        if p[0] not in string.ascii_lowercase + ".":
            return False

        if p[1] != "*":
            return False

        return self.helper(p[2:])


