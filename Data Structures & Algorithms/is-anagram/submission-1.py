class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        tlist = []
        for char in s:
            slist.append(char)
        for char in t:
            tlist.append(char)
        slist.sort()
        tlist.sort()
        if slist==tlist:
            return True
        else:
            return False