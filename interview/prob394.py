# 394 Decode String

# recursion. 5% solution
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "[" not in s:
            return s
        m = len(s)
        left  = []  # stack store indices of left brackit
        pairs = []  # store the partition of the string
        ks    = []  # store the number k
        i = 0
        while i < m: # increment i by hand
            c = s[i]
            if c == "[":
                left.append(i)
                i += 1
            elif c == "]":
                i0 = left.pop()
                n  = ks.pop()
                if not left: # outmost layer
                    pairs.append( (n, i0, i) )
                i += 1
            elif c in string.ascii_letters:
                word = ""
                j = i
                while j < m and s[j] in string.ascii_letters:
                    word += s[j]
                    j += 1
                if not left: # only store word at outmost layer
                    pairs.append( (1, word))
                i = j
            else: # digits
                j = i
                n = ""  #number k
                while j < m and s[j] in "0123456789":
                    n += s[j]
                    j += 1
                ks.append(int(n))
                i = j
                
        ans = ""
        for p in pairs:
            if len(p) == 2:
                ans += p[1] # a word
            else:
                n, l, r = p
                ans += self.decodeString(s[l+1:r]) * n
            
        return ans
            
# 40% solution
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "[" not in s:
            return s
        m = len(s)
        left  = []  # stack store indices of left brackit
        pairs = []  # store the partition of the string
        ks    = []  # store the number k
        i = 0
        while i < m: # increment i by hand
            c = s[i]
            if c == "[":
                left.append(i)
                i += 1
            elif c == "]":
                i0 = left.pop()
                n  = ks.pop()
                if not left:
                    word = self.decodeString(s[i0+1:i]) * n
                    pairs.append(word)
                i += 1
            elif c in string.ascii_letters:
                word = ""
                j = i
                while j < m and s[j] in string.ascii_letters:
                    word += s[j]
                    j += 1
                if not left: # only store word at outmost layer
                    pairs.append(word)
                i = j
            else: # digits
                j = i
                n = ""  #number k
                while j < m and s[j] in "0123456789":
                    n += s[j]
                    j += 1
                ks.append(int(n))
                i = j
                
        ans = "".join(pairs)
        return ans
 
