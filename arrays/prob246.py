class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        bad = ["2", "3", "4", "5", "7"]
        good = ["0", "1", "6", "8", "9"]

        m = {}
        m["0"] = "0"
        m["1"] = "1"
        m["6"] = "9"
        m["8"] = "8"
        m["9"] = "6"

        rev = []
        for c in num:
            if c in bad:
                return False
            else:
                rev.insert(0,  m[c])

        return "".join(rev) == num

