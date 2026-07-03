class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        final = ''
        for c in s:
            if c.isalnum():
                final += c
        return final == final[::-1]