class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n  = len(s1)
        m = len(s2)
        comp = []
        for c in s1:
            comp.append(c)
        comp.sort()
        for i in range(m):
            count = []
            substring = s2[i:i+n]
            for char in substring:
                count.append(char)
            count.sort()
            if count == comp:
                return True
        return False