# 383 Ransom Note

# 50%
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # build the dictionary
        mag = {}
        for char in magazine:
            mag[char] = mag.get(char, 0) + 1

        # use the dictionary
        for char in ransomNote:
            if char in mag:
                if mag[char] == 1:
                    del mag[char]
                else:
                    mag[char] -= 1
            else:
                return False

        return True

# 50%
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # build the dictionary
        mag = {}
        for char in magazine:
            mag[char] = mag.get(char, 0) + 1

        ransom = {}
        for char in ransomNote:
            ransom[char] = ransom.get(char, 0) + 1

        for key in ransom:
            if key not in mag:
                return False
            elif ransom[key] > mag[key]:
                return False
        return True

